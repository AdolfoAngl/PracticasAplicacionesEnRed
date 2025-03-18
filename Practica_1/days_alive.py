from datetime import datetime

fecha_nacimiento = input("Ingresa tu fecha de nacimiento (YYYY-MM-DD): ")
fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")

fecha_objetivo = datetime(2025, 3, 10)

dias_vividos = (fecha_objetivo - fecha_nacimiento).days

R = dias_vividos % 3

if R == 0:
    juego = "Buscaminas"
elif R == 1:
    juego = "Gato Dummy"
else:
    juego = "Memoria"

# Mostrar resultados
print(f"\nHas vivido {dias_vividos} días hasta el 10 de marzo de 2025.")
print(f"El resultado de {dias_vividos} % 3 es {R}, por lo que debes implementar el juego: {juego}")