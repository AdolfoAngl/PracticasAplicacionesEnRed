import socket

HOST = "localhost"  # Hostname o dirección IP del servidor
PORT = 65432  # Puerto del servidor
buffer_size = 1024

def mostrar_estado(mensaje):
    if mensaje == "S-6":
        print("Listo para recibir tiros")
    elif mensaje == "S-7":
        print("Mina pisada")
    elif mensaje == "S-8":
        print("Casilla ya liberada")
    elif mensaje == "S-9":
        print("Casilla liberada")
    elif mensaje == "S-10":
        print("Has ganado el juego!")
    else:
        print(f"Mensaje desconocido: {mensaje}")

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
        TCPClientSocket.connect((HOST, PORT))  # Envía una solicitud de conexión al servidor
        print("Conectado al servidor")

        while True:
            comando = input("Ingresa un comando (C-1 para principiante, C-2 para avanzado, o coordenadas como A,1): ")
            TCPClientSocket.sendall(comando.encode())  # Envía el comando al servidor

            data = TCPClientSocket.recv(buffer_size).decode()  # Recibe la respuesta del servidor
            mostrar_estado(data)

            if data == "S-7" or data == "S-10":  # Termina el juego si se pisa una mina o se gana
                break

except ConnectionError as e:
    print(f"Error de conexión: {e}")
except Exception as e:
    print(f"Ocurrió un error: {e}")