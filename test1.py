#MAQUINA CLIENTE CENTOS 8 172.31.29.110
import random
import json
import requests
import os

server_url = 'http://192.168.24.128:8080/backend/api'

def mostrar_menu():
    print("---- Menú ----")
    print("1. Ingresar ID del jugador")
    print("2. Ingresar ID del juego")
    print("3. Consultar juego disponible y estado del servidor")
    print("4. Realizar jugada")
    print("5. Consultar resultado del juego")
    print("6. Salir")

def ingresar_id_jugador():
    jugador_id = input("Ingrese el ID del jugador: ")
    return jugador_id

def ingresar_id_juego():
    juego_id = input("Ingrese el ID del juego: ")
    return juego_id

def consultar_juego_disponible_estado_servidor():
    response = requests.get(f"{server_url}/juego_disponible_estado")
    data = response.json()
    print(f"Juego disponible: {data['juego_disponible']}")
    print(f"Estado del servidor: {data['estado_servidor']}")
    print(f"ID del juego en curso: {data['juego_id']}")
    input("Presiona cualquier tecla para volver al menú...")

def realizar_jugada(jugador_id, juego_id):
    valor_jugada = random.randint(1, 100)
    jugada = {
        'jugador_id': jugador_id,
        'juego_id': juego_id,
        'valor_jugada': valor_jugada
    }
    response = requests.post(f"{server_url}/jugada", json=jugada)
    print("Jugada realizada:")
    print(response.text)
    input("Presiona cualquier tecla para volver al menú...")

def consultar_resultado_juego():
    response = requests.get(f"{server_url}/resultado")
    resultado_juego = response.json()
    print("---- Resultado del juego ----")
    for i in range(len(resultado_juego['jugadores'])):
        print(f"Jugador: {resultado_juego['jugadores'][i]} - Jugada: {resultado_juego['valores_jugadas'][i]}")
    print(f"Jugador ganador: {resultado_juego['jugador_ganador']}")
    print("Puntajes acumulados:")
    for jugador, puntaje in resultado_juego['puntajes'].items():
        print(f"{jugador}: {puntaje}")
    input("Presiona cualquier tecla para volver al menú...")

def main():
    jugador_id = ""
    juego_id = ""
    
    while True:
        os.system('clear')  # Limpiar la consola en sistemas Unix/Linux
        mostrar_menu()
        opcion = input("Ingrese el número de opción: ")
        if opcion == '1':
            jugador_id = ingresar_id_jugador()
            input("Presiona cualquier tecla para volver al menú...")
        elif opcion == '2':
            juego_id = ingresar_id_juego()
            input("Presiona cualquier tecla para volver al menú...")
        elif opcion == '3':
            consultar_juego_disponible_estado_servidor()
        elif opcion == '4':
            if not jugador_id or not juego_id:
                print("Debe ingresar el ID del jugador y el ID del juego primero.")
                input("Presiona cualquier tecla para volver al menú...")
            else:
                realizar_jugada(jugador_id, juego_id)
        elif opcion == '5':
            consultar_resultado_juego()
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == '__main__':
    main()
