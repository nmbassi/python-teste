# Importa as bibliotecas que serão utilizadas
import requests
import pandas as pd
import logging

# Função que realiza o GET na api com a url fornecida


def get_api_data(url):

    response = requests.get(url)

    if response.status_code == 200:  # Successful request
        data = response.json()  # Convert response to JSON format
        # Now you can work with the JSON data
    else:
        print("Error:", response.status_code)
    return data

# Função que trata os dados retornados no get realizado


def data_processing(data):
    df_people = pd.DataFrame(data['results'])  # Transforma em tabela os dados

    df_female = df_people[df_people['gender']
                          == 'female']  # Filtra o gênero feminino

    lista = ['name', 'hair_color', 'skin_color',
             'birth_year']  # Lista os campos desejados

    df_result = df_female[lista]  # Pega os campos da lista
    return df_result

# Função que gera o log


def log_generation(results):
    # configurando o Logging
    logging.basicConfig(filename='resultado.log',
                        level=logging.INFO, format='%(asctime)s - %(message)s')

    for index, row in results.iterrows():
        logging.info(f"Name: {row['name']}, Hair Color: {row['hair_color']}, Skin Color: {
                     row['skin_color']}, Birth Year: {row['birth_year']}")
