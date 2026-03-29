import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from io import StringIO
import time 

def extracaoDadosParaCsv():
    print("Testando robo")

    #configuracoes do selenium
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless==new")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")    
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-infobars")

    chrome_options.page_load_strategy = 'eager'

    servico = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=servico, options=chrome_options)

    dadosExtraidos = []
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"]

    try:
        url = "http://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html"
        print(f"Acessando a URL")
        driver.get(url)

        livros = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
        print("Livros encontrados, extraindo dados")

        for livro in livros:
            titulo = livro.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
            preco = livro.find_element(By.CSS_SELECTOR, "p.price_color").text
            disponibilidade = livro.find_element(By.CSS_SELECTOR, "p.instock.availability").text.strip()
            dadosExtraidos.append({"Título": titulo, "Preço": preco, "Disponibilidade": disponibilidade})

        #gravando dados
        df = pd.DataFrame(dadosExtraidos)
        df.to_csv("dados_extraidos.csv", index=False)
        print("Deu bom nos dados!")

    except Exception as e:
        print(f"Erro durante a extração: {e}")  
        
    finally:
        driver.quit()

if __name__ == "__main__":
    extracaoDadosParaCsv()