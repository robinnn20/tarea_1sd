
## Descripción
Este proyecto consiste en un script en Python que envía solicitudes a una API para resolver dominios. Utiliza un conjunto de datos descargado de Kaggle que contiene dominios, y realiza un número configurado de solicitudes a la API.

Descargar liberia 

```bash
pip install requests
```
instalara docker
```bash
sudo apt-get install docker-ce
```
Instalar docker-compose
```bash
sudo apt install docker-compose
```
Construir los contenedores
```bash
sudo docker-compose build 
```
Inicializar los contenedores
```bash
sudo docker-compose up -d 
```
Iniciar el generador de solicitudes
```bash
sudo python3 traffic_generator.py

