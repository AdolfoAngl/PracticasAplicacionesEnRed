import socket

HOST = "localhost"
PORT = 65432
buffer_size = 1024

def mostrar_estado(mensaje):
    if mensaje == "S-6":
        print("Listo para recibir tiros. Ingresa coordenadas en formato LetraNúmero, por ejemplo: A1")
    elif mensaje == "S-7":
        print("Mina pisada")
    elif mensaje == "S-8":
        print("Casilla ya liberada")
    elif mensaje == "S-9":
        print("Casilla liberada")
    elif mensaje == "S-10":
        print("Has ganado el juego!")
    elif mensaje == "S-11":
        print("Coordenadas fuera del rango, intenta de nuevo")
    else:
        print(f"Mensaje desconocido: {mensaje}")

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
        TCPClientSocket.connect((HOST, PORT))
        print("Conectado al servidor")
        print("Selecciona la dificultad: \nC-1: Principiante (9x9, 10 minas) \nC-2: Avanzado (16x16, 40 minas)")

        while True:
            comando = input("Ingresa tu selección o una coordenada (Ej: A1): ")
            TCPClientSocket.sendall(comando.encode())

            data = TCPClientSocket.recv(buffer_size).decode()
            mostrar_estado(data)

            if data == "S-7" or data == "S-10":
                break

except ConnectionError as e:
    print(f"Error de conexión: {e}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
