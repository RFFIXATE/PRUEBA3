#MAQUINA SERVIDOR LSO RHEL 8 192.168.24.128

from bottle import get, post, request, route, run, template
import random
import csv

jugadas_csv = 'jugadas.csv'
estado_servidor = 'disponible'
juego_en_curso = ''
numero_jugada_actual = 0

@post('/backend/api/jugada/<id_juego>')

def recibir_jugada(id_juego):
    jugador_id = request.forms.get('jugador_id')
    valor_jugada = request.forms.get('valor_jugada')
    print(f"Jugador ID: {jugador_id}, Juego ID: {id_juego}, Valor de la jugada: {valor_jugada}")
    guardar_jugada(jugador_id, id_juego, valor_jugada)
    return template('<b>Jugada recibida. Jugador ID: {{jugador_id}}, Juego ID: {{id_juego}}, Valor de la jugada: {{valor_jugada}}</b>!', jugador_id=jugador_id, id_juego=id_juego, valor_jugada=valor_jugada)

@get('/backend/api/resultado')

def consultar_resultado_juego():
    jugadas = {}
    with open(jugadas_csv, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar la primera línea (encabezado)
        for row in reader:
            numero_jugada = row[3]
            if numero_jugada in jugadas:
                jugadas[numero_jugada].append({
                    'jugador_id': row[0],
                    'valor_jugada': row[2],
                    'jugador_ganador': row[4]
                })
            else:
                jugadas[numero_jugada] = [{
                    'jugador_id': row[0],
                    'valor_jugada': row[2],
                    'jugador_ganador': row[4]
                }]
    
    resultado = {
        'jugadas': jugadas,
        'puntajes': calcular_puntajes(jugadas)
    }

    return resultado

@get('/backend/api/estado')

def obtener_estado_servidor():
    return {
        'estado_servidor': estado_servidor,
        'juego_id': juego_en_curso,
        'numero_jugada_actual': numero_jugada_actual
    }

def guardar_jugada(jugador_id, juego_id, valor_jugada):
    global numero_jugada_actual
    numero_jugada_actual += 1
    jugador_ganador = determinar_jugador_ganador(juego_id, valor_jugada)
    datos_jugada = [jugador_id, juego_id, valor_jugada, numero_jugada_actual, jugador_ganador]
    with open(jugadas_csv, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(datos_jugada)

def calcular_puntajes(jugadas):
    puntajes = {}
    for jugada, datos in jugadas.items():
        for dato in datos:
            jugador_id = dato['jugador_id']
            valor_jugada = int(dato['valor_jugada'])
            if jugador_id in puntajes:
                puntajes[jugador_id] += valor_jugada
            else:
                puntajes[jugador_id] = valor_jugada
    return puntajes

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
