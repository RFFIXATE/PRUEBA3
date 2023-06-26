#MAQUINA SERVIDOR LSO RHEL 8 192.168.24.128

from bottle import get, post, request, route, run, template
import random
import csv

jugadas = []

@post('/backend/api/jugada')
def recibir_jugada():
    jugador_id = request.forms.get('jugador_id')
    juego_id = request.forms.get('juego_id')
    valor_jugada = request.forms.get('valor_jugada')
    num_jugada = len(jugadas) + 1
    jugada = {
        'jugador_id': jugador_id,
        'juego_id': juego_id,
        'valor_jugada': valor_jugada,
        'num_jugada': num_jugada
    }
    jugadas.append(jugada)
    escribir_jugada_csv(jugada)  # Escribir jugada en el archivo CSV
    return template('Jugada recibida: {{jugada}}', jugada=jugada)

@get('/backend/api/estado-servidor')
def obtener_estado_servidor():
    estado_servidor = 'disponible' if jugadas else 'ocupado'
    juego_en_curso = jugadas[-1]['juego_id'] if jugadas else 'N/A'
    return template('Estado del servidor:<br>Estado: {{estado}}<br>ID del juego en curso: {{juego}}',
                    estado=estado_servidor, juego=juego_en_curso)

@get('/backend/api/resultado-juego')
def obtener_resultado_juego():
    if len(jugadas) < 5:
        return template('Aún no hay suficientes jugadas para determinar un ganador.')
    
    jugadas_ordenadas = sorted(jugadas, key=lambda x: int(x['valor_jugada']), reverse=True)
    jugador_ganador = jugadas_ordenadas[0]['jugador_id']
    puntaje_acumulado = sum(int(jugada['valor_jugada']) for jugada in jugadas)
    
    return template('Resultado del juego:<br>Jugador ganador: {{ganador}}<br>Puntaje acumulado: {{puntaje}}',
                    ganador=jugador_ganador, puntaje=puntaje_acumulado)

def escribir_jugada_csv(jugada):
    with open('jugadas.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([jugada['jugador_id'], jugada['juego_id'], jugada['valor_jugada'], jugada['num_jugada']])

run(host='192.168.24.128', port=8080)
