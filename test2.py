#MAQUINA SERVIDOR LSO RHEL 8 192.168.24.128

from bottle import get, post, request
from bottle import route, run, template
from datetime import datetime
import csv

@post('/backend/api/jugada')

def recibir_jugada():
    data = request.json
    jugador_id = data.get('jugador_id')
    juego_id = data.get('juego_id')
    valor_jugada = data.get('valor_jugada')

    # Hacer algo con los datos recibidos, por ejemplo, almacenarlos en un archivo CSV
    with open('jugadas.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([jugador_id, juego_id, valor_jugada])

    return template('<b>Jugada recibida - Jugador ID: {{jugador_id}} - Juego ID: {{juego_id}} - Valor de la jugada: {{valor_jugada}}</b>!', jugador_id=jugador_id, juego_id=juego_id, valor_jugada=valor_jugada)

run(host='192.168.24.128', port=8080)

@get('/backend/api/resultado')

def obtener_resultado_juego():
    # Hacer algo para obtener los datos del juego y los jugadores
    # Por ejemplo, leer los datos desde el archivo CSV

    jugadores = []
    jugadas = []
    jugador_ganador = None
    puntajes = {}

    with open('jugadas.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            jugador_id, juego_id, valor_jugada = row[:3]
            jugadores.append(jugador_id)
            jugadas.append(valor_jugada)

            # Calcular puntajes acumulados
            if jugador_id in puntajes:
                puntajes[jugador_id] += int(valor_jugada)
            else:
                puntajes[jugador_id] = int(valor_jugada)

    # Obtener el jugador ganador
    if puntajes:
        jugador_ganador = max(puntajes, key=puntajes.get)

    return template('resultado_juego.tpl', jugadores=jugadores, jugadas=jugadas, jugador_ganador=jugador_ganador, puntajes=puntajes)

run(host='192.168.24.128', port=8080)

@get('/backend/api/estado')

def obtener_estado_servidor():
    estado = 'disponible'  # Estado del servidor: disponible
    juego_en_curso = None  # ID del juego en curso (si hay alguno)

    # Hacer algo para determinar el estado del servidor y el ID del juego en curso
    # Por ejemplo, verificar si hay algún juego en curso en base a los datos del archivo CSV

    return template('estado_servidor.tpl', estado=estado, juego_en_curso=juego_en_curso)

run(host='192.168.24.128', port=8080)
