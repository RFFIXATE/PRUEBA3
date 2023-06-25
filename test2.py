#MAQUINA SERVIDOR LSO RHEL 8 172.31.29.110

from bottle import get, post, request
from bottle import route, run, template
from datetime import datetime
import csv

jugadores = []
jugadas = []
jugador_ganador = ""
puntajes = {}

@post('/backend/api/jugada')

def recibir_jugada():
    jugador_id = request.forms.get('jugador_id')
    juego_id = request.forms.get('juego_id')
    valor_jugada = request.forms.get('valor_jugada')

    jugadores.append(jugador_id)
    jugadas.append(valor_jugada)

    if jugador_id in puntajes:
        puntajes[jugador_id] += 1
    else:
        puntajes[jugador_id] = 1

    if puntajes[jugador_id] == 5:
        jugador_ganador = jugador_id

    # Guardar los datos en un archivo CSV
    with open('jugadas.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([jugador_id, juego_id, valor_jugada, len(jugadas), jugador_ganador])

    return "Jugada recibida correctamente."

@get('/backend/api/resultado')

def obtener_resultado_juego():
    return template('resultado_juego.tpl', jugadores=jugadores, jugadas=jugadas, jugador_ganador=jugador_ganador, puntajes=puntajes)

@get('/backend/api/estado')

def obtener_estado_servidor():
    estado = 'disponible'  # Estado del servidor: disponible
    juego_en_curso = None  # ID del juego en curso (si hay alguno)

    # Hacer algo para determinar el estado del servidor y el ID del juego en curso
    # Por ejemplo, verificar si hay algún juego en curso en base a los datos del archivo CSV

    return template('estado_servidor.tpl', estado=estado, juego_en_curso=juego_en_curso)

run(host='172.31.29.110', port=8080)