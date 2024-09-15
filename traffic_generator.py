import requests
import csv
import random

# URL de la API a la que se enviarán las peticiones
api_url = 'http://127.0.0.1:5000/resolve'

# Ruta del archivo CSV descargado desde Kaggle
dataset_path = '3rd_lev_domains.csv'
max_requests = 50  # Número total de consultas a realizar
max_data_size = 50000  # Tamaño máximo del dataset

def generate_requests(dataset_path, max_requests, max_data_size):
    with open(dataset_path, mode='r', newline='\n') as file:
        reader = csv.reader(file)
        # Omitir la cabecera del CSV si la hay
        next(reader, None)

        # Leer los primeros 50,000 registros
        domains = [row[0] for idx, row in enumerate(reader) if idx < max_data_size]

        # Realizar alrededor de 75,000 consultas
        for _ in range(max_requests):
            # Elegir un dominio aleatorio
            domain = random.choice(domains)
            response = requests.post(api_url, json={'domain': domain})
            print(f'Sent: {domain} - Status Code: {response.status_code}')
            print(f'Response: {response.text}')  # Usar .text para respuestas que no son JSON

if __name__ == '__main__':
    generate_requests(dataset_path, max_requests, max_data_size)
