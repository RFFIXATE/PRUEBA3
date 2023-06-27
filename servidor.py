#MAQUINA SERVIDOR LSO RHEL 8 192.168.24.128
#pip3 install bottle
#pip3 install csv

from bottle import post, get, run, template, request
import random
import csv

juego_id_generado = None
jugadores = []
jugadas = []
jugador_ganador = ""
puntajes = {}
estado_servidor = {
    'estado': 'disponible',
    'juego_en_curso': None
}

#servidor responde a jugada
@post('/backend/api/jugada')
def recibir_jugada():
    global jugador_ganador  

    jugador_id = request.json.get('jugador_id')
    juego_id = request.json.get('juego_id')
    valor_jugada = request.json.get('valor_jugada')

    jugadores.append(jugador_id)
    jugadas.append(valor_jugada)

    if jugador_id in puntajes:
        puntajes[jugador_id] += valor_jugada
    else:
        puntajes[jugador_id] = valor_jugada

    if jugador_ganador == "" or puntajes[jugador_id] > puntajes[jugador_ganador]:
        jugador_ganador = jugador_id

    escribir_jugada_csv(jugador_id, juego_id, valor_jugada)

    return template('<b>Jugada recibida correctamente. Jugador: {{jugador_id}}, Juego: {{juego_id}}, Valor: {{valor_jugada}}</b>', jugador_id=jugador_id, juego_id=juego_id, valor_jugada=valor_jugada)


#Servidor obtiene resultado
@get('/backend/api/resultado')

def obtener_resultado_juego():
    resultado = {
        'jugadores': jugadores,
        'jugadas': jugadas,
        'jugador_ganador': jugador_ganador,
        'puntajes': puntajes
    }
    return resultado

#servidor obtiene el estado de si mismo
@get('/backend/api/estado')
def obtener_estado_servidor():
    estado_servidor['juego_en_curso'] = str(estado_servidor['juego_en_curso'])
    return estado_servidor

#servidor realiza una solicitud de juego
@post('/backend/api/juego')

def iniciar_juego():
    estado_servidor['estado'] = 'ocupado'
    estado_servidor['juego_en_curso'] = random.randint(1, 100)
    estado_servidor['juego_en_curso'] = juego_id_generado
    return f"Juego iniciado. ID del juego en curso: {juego_id_generado}"

def escribir_jugada_csv(jugador_id, juego_id, valor_jugada):
    with open('jugadas.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([jugador_id, juego_id, valor_jugada])

run(host='192.168.24.128', port=8080)