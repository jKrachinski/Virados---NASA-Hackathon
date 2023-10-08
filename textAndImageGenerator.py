import json
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import date, datetime, timedelta
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNDUyNTQwYzItZjRmZC00ZTk4LTk5NzEtNDNkMjFkNTQ0NjZhIiwidHlwZSI6ImFwaV90b2tlbiJ9.y5u_w4MIkY4h4aZSej-3i7owPobdLd-H8A0BKCgyuhI"}

def generate_image(prompt : str):
    url = "https://api.edenai.run/v2/image/generation"              	 
    payload = {
    "providers": "openai",
    "text": prompt,
    "resolution" : "512x512",
    "num_images": 5
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    image = result['openai']['items']
    
    print(image[0]['image_resource_url'])
    return image[0]['image_resource_url']

def generate_text(prompt : str):
    url ="https://api.edenai.run/v2/text/generation"
    payload = {
        "providers": "openai,cohere",
        "text": prompt,
        "temperature" : 1,
        "max_tokens" : 1000
        }

    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)
    resposta = result['openai']['generated_text']
    print(resposta)

    with open("saida.txt", "w") as file:
        file.write(resposta)

caracteristicas_do_planeta = "Quente, habitado por vida inteligente no mesmo nível tecnológico atual, grandes quantidades de água, natureza abundante"

palavras_chave = f"exoplaneta, habitável, {caracteristicas_do_planeta}"
descricao = f"Gere uma descrição realística de como seria morar em um exoplaneta com as seguintes características: {caracteristicas_do_planeta}.\n Essa descrição precisa ter, no mínimo, 500 palavras"
resumo = f'Gere uma breve descrição de um planeta com as seguintes características: {caracteristicas_do_planeta}'



#generate_text(descricao)
img_link = generate_image(palavras_chave)

options = Options()
options.add_experimental_option("detach", True)

# é utilizado o chrome para enviar as mensagens
driver = webdriver.Chrome(options=options)
driver.get(img_link)
driver.implicitly_wait(600)
driver.close()