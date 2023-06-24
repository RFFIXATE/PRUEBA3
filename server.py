#pip install bottle
#pip3 install bottle


from bottle import Bottle, request, template

app = Bottle()

# Lista para almacenar los datos de las jugadas
jugadas = []

# Ruta para recibir una jugada mediante POST
@app.post('/jugada')
def recibir_jugada():
    jugador_id = request.forms.get('jugador_id')
    juego_id = request.forms.get('juego_id')
    valor_jugada = request.forms.get('valor_jugada')

    # Guardar la jugada en la lista de jugadas
    jugadas.append({
        'jugador_id': jugador_id,
        'juego_id': juego_id,
        'valor_jugada': valor_jugada
    })

    return 'Jugada recibida'

# Ruta para mostrar el resultado del juego en una vista HTML
@app.get('/resultado')
def mostrar_resultado():
    # Aquí debes implementar la lógica para calcular el resultado del juego
    # y generar una vista HTML con los datos requeridos
    # Puedes utilizar la función 'template' para renderizar una plantilla HTML

    # Ejemplo de cómo se podría renderizar una plantilla con los datos
    jugadores = ['Jugador 1', 'Jugador 2']
    jugadas = [{'jugador_id': '1', 'valor_jugada': '5'}, {'jugador_id': '2', 'valor_jugada': '8'}]
    jugador_ganador = 'Jugador 2'
    puntaje_acumulado = {'Jugador 1': 10, 'Jugador 2': 15}

    return template('resultado.tpl', jugadores=jugadores, jugadas=jugadas, jugador_ganador=jugador_ganador, puntaje_acumulado=puntaje_acumulado)

# Ruta para mostrar el estado del servidor
@app.get('/estado')
def mostrar_estado():
    # Aquí debes implementar la lógica para determinar el estado del servidor
    # y devolverlo como una respuesta en formato JSON

    # Ejemplo de cómo se podría devolver el estado en formato JSON
    estado_servidor = 'ocupado'
    juego_en_curso = 'ABC123'

    return {
        'estado_servidor': estado_servidor,
        'juego_en_curso': juego_en_curso
    }

# Ejecutar la aplicación en el servidor local
if __name__ == '__main__':
    app.run(host='172.31.29.110', port=8080)
