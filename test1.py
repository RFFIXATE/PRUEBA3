#MAQUINA CLIENTE CENTOS 8 172.31.29.110
import random
import requests
import msvcrt

def ingresar_jugador():
    jugador_id = input("Ingrese el ID del jugador: ")
    return jugador_id

def ingresar_juego():
    juego_id = input("Ingrese el ID del juego: ")
    return juego_id

def consultar_juego_disponible():
    url = 'http://192.168.24.128:8080/backend/api/estado'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        estado_servidor = data.get('estado_servidor')
        juego_id = data.get('juego_id')
        numero_jugada_actual = data.get('numero_jugada_actual')
        print(f"Estado del servidor: {estado_servidor}")
        print(f"ID del juego disponible: {juego_id}")
        print(f"Número de jugada actual: {numero_jugada_actual}")
    else:
        print("Error al consultar el estado del servidor")

def realizar_jugada(jugador_id, juego_id):
    rango_inicial = 10
    rango_final = 100
    numero = random.randint(rango_inicial, rango_final)
    print(f"Número generado: {numero}")

    url = f'http://192.168.24.128:8080/backend/api/jugada/{juego_id}'

    datos_jugada = {
        'jugador_id': jugador_id,
        'valor_jugada': numero
    }

    response = requests.post(url, data=datos_jugada)

    if response.status_code == 200:
        print("Jugada enviada con éxito")
    else:
        print("Error al enviar la jugada")

def consultar_resultado_juego():
    url = 'http://192.168.24.128:8080/backend/api/resultado'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        jugadas = data.get('jugadas')
        puntajes = data.get('puntajes')

        print("Resultado del juego:")
        for numero_jugada, datos_jugadas in jugadas.items():
            print(f"Jugada #{numero_jugada}")
            for dato in datos_jugadas:
                jugador_id = dato['jugador_id']
                valor_jugada = dato['valor_jugada']
                jugador_ganador = dato['jugador_ganador']
                print(f"Jugador: {jugador_id}, Valor de la jugada: {valor_jugada}, Ganador: {jugador_ganador}")
            print("-------")
        
        print("Puntaje acumulado de los jugadores:")
        for jugador_id, puntaje in puntajes.items():
            print(f"Jugador: {jugador_id}, Puntaje: {puntaje}")
    else:
        print("Error al consultar el resultado del juego")

def mostrar_menu():
    print("----- MENU -----")
    print("1. Ingresar ID del jugador")
    print("2. Ingresar ID del juego")
    print("3. Consultar juego disponible")
    print("4. Realizar jugada")
    print("5. Consultar resultado del juego")
    print("0. Salir")

jugador_id = ""
juego_id = ""

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        jugador_id = ingresar_jugador()
        msvcrt.getch()
    elif opcion == "2":
        juego_id = ingresar_juego()
        msvcrt.getch()
    elif opcion == "3":
        consultar_juego_disponible()
        msvcrt.getch()
    elif opcion == "4":
        if jugador_id and juego_id:
            realizar_jugada(jugador_id, juego_id)
        else:
            print("Ingrese el ID del jugador y del juego antes de realizar la jugada")
        msvcrt.getch()
    elif opcion == "5":
        consultar_resultado_juego()
        msvcrt.getch()
    elif opcion == "0":
        break
    else:
        print("Opción inválida. Intente nuevamente.")
        msvcrt.getch()
