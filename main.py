# Importa as functions utilizadas
from functions import get_api_data, data_processing, log_generation

# Passa o endpoint que será utilizado na função
url = 'https://swapi.dev/api/people'

# Função de encapsulamento


def main(url):
    data = get_api_data(url)
    table_results = data_processing(data)
    log_generation(table_results)


main(url)
