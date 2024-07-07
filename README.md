# projeto_livro
Coletor de Dados de Livros na Amazon
Este script em Python utiliza Selenium para coletar informações de livros na Amazon Brasil sobre automação. Os dados são armazenados em arquivos CSV e Excel para análise posterior.

Requisitos
Python 3.12.1
Bibliotecas Python:
Selenium
Pandas
Webdriver Manager
openpyxl (para exportar para Excel)

Instalação
Clone o repositório:

bash
Copiar código
git clone https://github.com/Marvingms7/projeto_livro


cd projeto_livro


Instale as dependências.

Copiar código:
pip install -r requirements.txt
Certifique-se de estar utilizando um ambiente virtual Python se necessário (venv).

Configure o WebDriver:

O script usa o WebDriver do Chrome. Certifique-se de que o ChromeDriver está instalado corretamente. O WebDriver Manager pode ajudar a gerenciar a instalação automaticamente.

Utilização:
Execute o script main.py

Copiar código:
python main.py

O script abrirá o Chrome em modo headless, acessará a Amazon Brasil e pesquisará por livros sobre automação.

Os dados dos livros (Título, Autor, Preço, Nota e Avaliações) serão coletados da primeira página de resultados.

Os dados serão salvos nos arquivos livros_amazon.csv e livros_amazon.xlsx no diretório do projeto.

Notas
O script foi desenvolvido para fins educacionais em um processo seletivo, pode necessitar de ajustes dependendo de mudanças na estrutura da Amazon.
Certifique-se de respeitar os termos de serviço da Amazon ao realizar scraping de dados.
