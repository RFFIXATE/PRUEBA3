#MAQUINA CLIENTE CENTOS 8 172.31.29.110
import random
import json
import requests

def ingresar_id_jugador():
    jugador_id = input("Ingrese el ID del jugador: ")
    return jugador_id

def ingresar_id_juego():
    juego_id = input("Ingrese el ID del juego: ")
    return juego_id

def consultar_juego_disponible():
    url = 'http://172.31.29.110:8080/backend/api/estado'
    response = requests.get(url)
    if response.status_code == 200:
        estado_servidor = response.json()
        estado = estado_servidor.get('estado')
        juego_en_curso = estado_servidor.get('juego_en_curso')
        print(f"Estado del servidor: {estado}")
        print(f"ID del juego en curso: {juego_en_curso}")
    else:
        print("No se pudo obtener el estado del servidor.")

def realizar_jugada(jugador_id, juego_id):
    rango_inicial = 10
    rango_final = 100

    numero = random.randint(rango_inicial, rango_final)
    print(f"Número de jugada generado: {numero}")

    jugada = {
        'jugador_id': jugador_id,
        'juego_id': juego_id,
        'valor_jugada': numero
    }

    url = 'http://172.31.29.110:8080/backend/api/jugada'
    response = requests.post(url, json=jugada)

    if response.status_code == 200:
        print("Jugada enviada correctamente.")
    else:
        print("Error al enviar la jugada.")

def consultar_resultado_juego():
    url = 'http://172.31.29.110:8080/backend/api/resultado'
    response = requests.get(url)
    if response.status_code == 200:
        resultado_juego = response.text
        print(resultado_juego)
    else:
        print("No se pudo obtener el resultado del juego.")

def mostrar_menu():
    menu = """
    --- Menú ---
    1. Ingresar ID del jugador
    2. Ingresar ID del juego
    3. Consultar juego disponible
    4. Realizar jugada
    5. Consultar resultado del juego
    6. Salir
    """

    print(menu)

def main():
    jugador_id = None
    juego_id = None

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            jugador_id = ingresar_id_jugador()
        elif opcion == "2":
            juego_id = ingresar_id_juego()
        elif opcion == "3":
            consultar_juego_disponible()
        elif opcion == "4":
            if jugador_id and juego_id:
                realizar_jugada(jugador_id, juego_id)
            else:
                print("Debe ingresar el ID del jugador y del juego antes de realizar una jugada.")
        elif opcion == "5":
            consultar_resultado_juego()
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == '__main__':
    main()
