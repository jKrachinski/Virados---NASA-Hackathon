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
import pandas as pd
import os

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNDUyNTQwYzItZjRmZC00ZTk4LTk5NzEtNDNkMjFkNTQ0NjZhIiwidHlwZSI6ImFwaV90b2tlbiJ9.y5u_w4MIkY4h4aZSej-3i7owPobdLd-H8A0BKCgyuhI"}

def generate_image(prompt : str):
    url = "https://api.edenai.run/v2/image/generation"              	 
    payload = {
    "providers": "openai",
    "text": prompt,
    "resolution" : "512x512",
    "num_images": 1
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
        "max_tokens" : 1500
        }

    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)
    resposta = result['openai']['generated_text']
    print(resposta)
    return(resposta)

caracteristicas_do_planeta = "Quente, habitado por vida inteligente no mesmo nível tecnológico atual, grandes quantidades de água, natureza abundante"

options = Options()
options.add_experimental_option("detach", True)

class CreateDescription:
    def __init__(self, key_words):
        caracteristicas_do_planeta_para_imagem = f"exoplaneta, habitável, {key_words}"
        descricao_palavras = f"Gere uma descrição realística e científica de como seria morar em um exoplaneta com as seguintes características: {key_words}.\n A tecnologia neste planeta não é mais avançada que a atual. Essa descrição precisa ter, no mínimo, 500 palavras"
        resumo_planeta = f'Gere uma breve descrição de um planeta com as seguintes características: {key_words}. Essa descricao deve ser feita em 20 palavras ou menos'
        
        imagem_link = generate_image(caracteristicas_do_planeta_para_imagem)
        descricao_500 = generate_text(descricao_palavras)
        resuminho = generate_text(resumo_planeta)
        
        dictionary = {
            "500palavras":descricao_500,
            "descricaoBreve":resuminho,
            "link_imagem":imagem_link
        }
        
        df = pd.DataFrame(dictionary, index=[0])
        
        i = 1
        while(True):
            if os.path.isfile(f"generatedResponse{i}.json"):
                i += 1
            else:
                break
        df.to_json(f"generatedResponse{i}.json")
        
        
        #downloads the AI generated image
        driver = webdriver.Chrome(options=options)
        driver.get(imagem_link)
        driver.implicitly_wait(600)
        driver.close()
        
test = CreateDescription(caracteristicas_do_planeta)