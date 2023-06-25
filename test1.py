#MAQUINA CLIENTE CENTOS 8 172.31.29.110
import random
import json
import requests

rango_inicial = 10
rango_final = 100

# Generar el número aleatorio
numero = random.randint(rango_inicial, rango_final)
print(numero)

# Construir el diccionario con los datos de la jugada
jugada = {
    'jugador_id': '',
    'juego_id': '',
    'valor_jugada': numero
}

# Enviar la solicitud POST al servidor
url = 'http://172.31.29.110:8080/backend/api/jugada/1'
enviar = requests.post(url, json=jugada)
print('El servidor responde:', enviar.text)

# Obtener los datos del servidor y asignarlos a las variables correspondientes
respuesta = enviar.json()
jugador_id = respuesta.get('jugador_id')
juego_id = respuesta.get('juego_id')

# Actualizar el diccionario de jugada con los valores recibidos del servidor
jugada['jugador_id'] = jugador_id
jugada['juego_id'] = juego_id

# Imprimir la jugada con los valores asignados
print('Jugada:', jugada)
