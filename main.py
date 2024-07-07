import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Configurações do WebDriver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Executar o Chrome no modo headless
driver = webdriver.Chrome(service=service, options=options)

# Acesse a Amazon Brasil e pesquise por livros sobre automação
driver.get("https://www.amazon.com.br/")
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("livros sobre automacao")
search_box.submit()

time.sleep(3)  # Aguarde alguns segundos para a página carregar

books = []

# Coleta informações dos livros na primeira página de resultados
for book in driver.find_elements(By.CSS_SELECTOR, ".s-main-slot .s-result-item"):
    try:
        title = book.find_element(By.CSS_SELECTOR, "h2 .a-link-normal").text
    except:
        title = "N/A"
    
    try:
        author = book.find_element(By.CSS_SELECTOR, ".a-color-secondary .a-size-base+ .a-size-base").text
    except:
        author = "N/A"
    
    # Capturar o preço principal
    try:
        price_whole = book.find_element(By.CSS_SELECTOR, ".a-price .a-price-whole").text
        price_fraction = book.find_element(By.CSS_SELECTOR, ".a-price .a-price-fraction").text
        price = f"{price_whole},{price_fraction}"
         # Verificar se o preço é de kindleUnlimited "0,00" e também capturar o preço de compra normal
        if price == "0,00":
            alt_price_text = book.find_element(By.CSS_SELECTOR, "div[data-cy='secondary-offer-recipe'] .a-row.a-size-base.a-color-secondary span").text
            # Plus: Fiz a utilização da biblioteca "re" para filtrar apenas os números e mostrar os dois valores caso seja kindle 
            price_match = re.search(r'R\$\s*([\d,]+)', alt_price_text)
            if price_match:
                alt_price = price_match.group(1)
            else:
                alt_price = "N/A"
            price = f"Kindle Unlimited: {price} Ou para comprar: R$ {alt_price}"
    except:
        price = "N/A"
    
    try:
        rating = book.find_element(By.CSS_SELECTOR, ".a-icon-alt").get_attribute("innerHTML")
    except:
        rating = "N/A"
    
    try:
        reviews = book.find_element(By.CSS_SELECTOR, ".a-size-small .a-link-normal").text

        if reviews == "Capa Comum":
            # Clicar no título para acessar a página do produto
            book.find_element(By.CSS_SELECTOR, ".a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal").click()
            
            # Aguardar carregamento da página do produto
            time.sleep(3)
            
            # Tentativa de capturar o preço da capa comum na página do produto
            try:
                price = driver.find_element(By.CSS_SELECTOR, ".a-size-base.a-color-price").text
            except:
                price = "N/A"
            
            # Voltar para a página de resultados
            driver.back()
        elif reviews == "Kindle":
            # Clicar no título para acessar a página do produto
            book.find_element(By.CSS_SELECTOR, ".a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal").click()
            
            # Aguardar carregamento da página do produto
            time.sleep(3)
            
            # Tentativa de capturar o preço da capa comum na página do produto
            try:
                price = driver.find_element(By.CSS_SELECTOR, ".a-size-base.a-color-price").text
            except:
                price = "N/A"
            
            # Voltar para a página de resultados
            driver.back()
        else:
            reviews = book.find_element(By.CSS_SELECTOR, ".a-size-small .a-link-normal").text
    except:
        reviews = "N/A"
        
    books.append({
        "Título": title,
        "Autor": author,
        "Preço": price,
        "Nota": rating,
        "Avaliações": reviews
    })

# Feche o navegador
driver.quit()

# Crie um DataFrame pandas e salve os dados em um arquivo CSV
df = pd.DataFrame(books)
df.sort_values("Título", inplace=True)
df.to_csv("livros_amazon.csv", index=False)

print("Dados coletados e salvos em livros_amazon.csv")
