#MAQUINA SERVIDOR LSO RHEL 8 172.31.29.110

from bottle import get, post, request
from bottle import route, run, template
from datetime import datetime

@post('/backend/api/jugada/1')

def recibir_jugada():

    #jugada = request.forms.get('jugada')
    jugada = 'TEST'
    print (request.body)
    return template('<b>Jugada 1 recibida {{jugada}}</b>!', jugada=jugada)

run(host='172.31.29.110', port=8080)
