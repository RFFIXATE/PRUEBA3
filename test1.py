#MAQUINA CLIENTE CENTOS 8 192.168.24.128
import random
import json
import requests
import os


jugador_id = None
juego_id = None

def ingresar_id_jugador():
    global jugador_id
    jugador_id = input("Ingrese el ID del jugador: ")
    if not jugador_id:
        print("ERROR: El ID del jugador no puede estar vacío.")
        ingresar_id_jugador()

def ingresar_id_juego():
    global juego_id
    juego_id = input("Ingrese el ID del juego: ")
    if not juego_id:
        print("ERROR: El ID del juego no puede estar vacío.")
        ingresar_id_juego()

def consultar_juego_disponible():
    url = 'http://192.168.24.128:8080/backend/api/estado'
    response = requests.get(url)
    if response.status_code == 200:
        estado_servidor = response.json()
        estado = estado_servidor.get('estado')
        juego_en_curso = estado_servidor.get('juego_en_curso')
        if juego_en_curso is not None:
            print(f"Estado del servidor: {estado}")
            print(f"ID del juego en curso: {juego_en_curso}")
            if juego_id is not None:
                print(f"ID del juego ingresado: {juego_id}")
        else:
            print("No hay juego en curso.")
    else:
        print("No se pudo obtener el estado del servidor.")



def realizar_jugada():
    if not jugador_id:
        print("ERROR: No se ha ingresado el ID del jugador.")
        return
    if not juego_id:
        print("ERROR: No se ha ingresado el ID del juego.")
        return
    
    rango_inicial = 10
    rango_final = 100

    numero = random.randint(rango_inicial, rango_final)
    print(f"Número de jugada generado: {numero}")

    jugada = {
        'jugador_id': jugador_id,
        'juego_id': juego_id,
        'valor_jugada': numero
    }

    url = 'http://192.168.24.128:8080/backend/api/jugada'
    response = requests.post(url, json=jugada)

    if response.status_code == 200:
        print("Jugada enviada correctamente.")
    else:
        print("Error al enviar la jugada.")

def consultar_resultado_juego():
    url = 'http://192.168.24.128:8080/backend/api/resultado'
    response = requests.get(url)
    if response.status_code == 200:
        resultado_juego = response.json()
        print("Nombre de los jugadores:", resultado_juego['jugadores'])
        print("Valores de las jugadas:", resultado_juego['jugadas'])
        print(f"ID del juego: {juego_id}")
        print("Jugador Ganador:", resultado_juego['jugador_ganador'])
        print("Puntaje acumulado de los jugadores:", resultado_juego['puntajes'])
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
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_id_jugador()
            input("Presione Enter para continuar...")
            os.system('clear' if os.name == 'posix' else 'cls')  # Limpia la pantalla
        elif opcion == "2":
            ingresar_id_juego()
            input("Presione Enter para continuar...")
            os.system('clear' if os.name == 'posix' else 'cls')  # Limpia la pantalla
        elif opcion == "3":
            consultar_juego_disponible()
            input("Presione Enter para continuar...")
            os.system('clear' if os.name == 'posix' else 'cls')  # Limpia la pantalla
        elif opcion == "4":
            realizar_jugada()
            input("Presione Enter para continuar...")
            os.system('clear' if os.name == 'posix' else 'cls')  # Limpia la pantalla
        elif opcion == "5":
            consultar_resultado_juego()
            input("Presione Enter para continuar...")
            os.system('clear' if os.name == 'posix' else 'cls')  # Limpia la pantalla
        elif opcion == '6':
            input("usted selecciono salir... presione para confirmar")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            input("Presione Enter para continuar...")
            os.system('clear' if os.name == 'posix' else 'cls')  # Limpia la pantalla

if __name__ == '__main__':
    main()