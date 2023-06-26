#MAQUINA SERVIDOR LSO RHEL 8 192.168.24.128

from bottle import post, get, run, template, request
import random
import csv

jugadores = []
jugadas = []
jugador_ganador = ""
puntajes = {}
estado_servidor = {
    'estado': 'disponible',
    'juego_en_curso': None
}

@post('/backend/api/jugada')

def recibir_jugada():
    jugador_id = request.json.get('jugador_id')
    juego_id = request.json.get('juego_id')
    valor_jugada = request.json.get('valor_jugada')

    jugadores.append(jugador_id)
    jugadas.append(valor_jugada)

    if jugador_id in puntajes:
        puntajes[jugador_id] += 1
    else:
        puntajes[jugador_id] = 1

    if puntajes[jugador_id] == 5:
        jugador_ganador = jugador_id

    escribir_jugada_csv(jugador_id, juego_id, valor_jugada)

    return template('<b>Jugada recibida correctamente. Jugador: {{jugador_id}}, Juego: {{juego_id}}, Valor: {{valor_jugada}}</b>', jugador_id=jugador_id, juego_id=juego_id, valor_jugada=valor_jugada)


@get('/backend/api/resultado')

def obtener_resultado_juego():
    resultado = {
        'jugadores': jugadores,
        'jugadas': jugadas,
        'jugador_ganador': jugador_ganador,
        'puntajes': puntajes
    }
    return resultado

@get('/backend/api/estado')

def obtener_estado_servidor():
    return estado_servidor

@post('/backend/api/juego')

def iniciar_juego():
    estado_servidor['estado'] = 'ocupado'
    estado_servidor['juego_en_curso'] = random.randint(1, 100)

    return "Juego iniciado."

def escribir_jugada_csv(jugador_id, juego_id, valor_jugada):
    with open('jugadas.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([jugador_id, juego_id, valor_jugada])

run(host='192.168.24.128', port=8080)