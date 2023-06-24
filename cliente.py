#sudo yum install -y git
#sudo yum install -y python3-pip
#pip3 install bottle, request
import requests

# URL base del servidor
base_url = '172.31.29.120:8080'

def ingresar_id_jugador():
    jugador_id = input('Ingrese el ID del jugador: ')
    return jugador_id

def ingresar_id_juego():
    juego_id = input('Ingrese el ID del juego: ')
    return juego_id

def consultar_juego_disponible():
    url = f'{base_url}/estado'
    response = requests.get(url)
    estado_servidor = response.json()['estado_servidor']
    juego_en_curso = response.json()['juego_en_curso']

    if estado_servidor == 'disponible':
        if juego_en_curso:
            print(f'El juego {juego_en_curso} está en curso')
        else:
            print('No hay juegos en curso')
    else:
        print('El servidor está ocupado')

def realizar_jugada(jugador_id, juego_id):
    valor_jugada = input('Ingrese el valor de la jugada (entre 1 y 10): ')
    url = f'{base_url}/jugada'
    data = {
        'jugador_id': jugador_id,
        'juego_id': juego_id,
        'valor_jugada': valor_jugada
    }
    response = requests.post(url, data=data)
    print(response.text)

def consultar_resultado_juego():
    url = f'{base_url}/resultado.tpl'
    response = requests.get(url)
    print(response.text)

def mostrar_menu():
    menu = '''
    Menú:
    1. Ingresar ID del jugador
    2. Ingresar ID del juego
    3. Consultar juego disponible
    4. Realizar jugada
    5. Consultar resultado del juego
    6. Salir
    '''
    print(menu)

jugador_id = None
juego_id = None

while True:
    mostrar_menu()
    opcion = input('Ingrese una opción: ')

    if opcion == '1':
        jugador_id = ingresar_id_jugador()
    elif opcion == '2':
        juego_id = ingresar_id_juego()
    elif opcion == '3':
        consultar_juego_disponible()
    elif opcion == '4':
        if jugador_id and juego_id:
            realizar_jugada(jugador_id, juego_id)
        else:
            print('Debe ingresar el ID del jugador y el ID del juego primero')
    elif opcion == '5':
        consultar_resultado_juego()
    elif opcion == '6':
        break
    else:
        print('Opción inválida')
