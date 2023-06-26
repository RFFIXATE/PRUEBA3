#MAQUINA SERVIDOR LSO RHEL 8 192.168.24.128

from bottle import get, post, request
from bottle import route, run, template
import random
import csv

jugadas_csv = 'jugadas.csv'

@post('/backend/api/jugada/<id_juego>')
def recibir_jugada(id_juego):
    jugador_id = request.forms.get('jugador_id')
    valor_jugada = request.forms.get('valor_jugada')
    print(f"Jugador ID: {jugador_id}, Juego ID: {id_juego}, Valor de la jugada: {valor_jugada}")
    guardar_jugada(jugador_id, id_juego, valor_jugada)
    return template('<b>Jugada recibida. Jugador ID: {{jugador_id}}, Juego ID: {{id_juego}}, Valor de la jugada: {{valor_jugada}}</b>!', jugador_id=jugador_id, id_juego=id_juego, valor_jugada=valor_jugada)

def guardar_jugada(jugador_id, juego_id, valor_jugada):
    numero_jugada = obtener_numero_jugada()
    jugador_ganador = determinar_jugador_ganador(juego_id, valor_jugada)
    datos_jugada = [jugador_id, juego_id, valor_jugada, numero_jugada, jugador_ganador]
    with open(jugadas_csv, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(datos_jugada)

def obtener_numero_jugada():
    with open(jugadas_csv, 'r') as file:
        reader = csv.reader(file)
        numero_jugadas = len(list(reader))
    return numero_jugadas + 1

def determinar_jugador_ganador(juego_id, valor_jugada):
    puntajes = {}
    with open(jugadas_csv, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == juego_id:
                jugador_id = row[0]
                valor_actual = int(row[2])
                if jugador_id in puntajes:
                    puntajes[jugador_id] += valor_actual
                else:
                    puntajes[jugador_id] = valor_actual
    
    if puntajes:
        max_puntaje = max(puntajes.values())
        jugadores_max = [jugador_id for jugador_id, puntaje in puntajes.items() if puntaje == max_puntaje]
        return ", ".join(jugadores_max)
    else:
        return ""

run(host='192.168.24.128', port=8080)
