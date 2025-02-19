import random

# Pedir al usuario los valores de entrada
rango_min = int(input("Ingrese el número mínimo del rango: "))
rango_max = int(input("Ingrese el número máximo del rango: "))
cantidad = int(input("Ingrese la cantidad de números aleatorios a generar: "))

# Generar números aleatorios dentro del rango
numeros = [random.randint(rango_min, rango_max) for _ in range(cantidad)]

# Mostrar los números generados
print("Números generados:", numeros)

# Calcular la suma total
suma_total = sum(numeros)
print("Suma total:", suma_total)