#MAQUINA SERVIDOR LSO RHEL 8 172.31.29.110

from bottle import get, post, request
from bottle import route, run, template
from datetime import datetime

@post('/backend/api/jugada/1')

def recibir_jugada():
    data = request.json
    jugador_id = data.get('jugador_id')
    juego_id = data.get('juego_id')
    valor_jugada = data.get('valor_jugada')

    # Hacer algo con los datos recibidos, por ejemplo, almacenarlos en una base de datos

    return template('<b>Jugada 1 recibida</b>! Jugador ID: {{jugador_id}}, Juego ID: {{juego_id}}, Valor de la jugada: {{valor_jugada}}',
                    jugador_id=jugador_id, juego_id=juego_id, valor_jugada=valor_jugada)

run(host='172.31.29.110', port=8080)
