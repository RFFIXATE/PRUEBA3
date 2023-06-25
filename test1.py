#MAQUINA CLIENTE CENTOS 8 172.31.29.110
import random
import json
import requests

rango_inicial=10
rango_final=100
#//PASO 1
numero=random.randint(rango_inicial,rango_final)
print(numero)

#//PASO 2
jugada = {
            'jugada':1,
            'valor':numero
        }

#//PASO 3
url = 'http://172.31.29.120:8080/backend/api/jugada/1'

enviar = requests.post(url, json=json.dumps(jugada))
print('El servidor responde: ', enviar.text)
