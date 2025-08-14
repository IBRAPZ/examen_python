# NUMERO 3

entrada = input("Escribe 4 números separados por comas: ")

# Separar los números y convertirlos a enteros
numeros = tuple(int(n) for n in entrada.split(","))

# Calcular promedio, máximo y mínimo
promedio = sum(numeros) / len(numeros)
maximo = max(numeros)
minimo = min(numeros)

# Mostrar resultados
print("Tupla:", numeros)
print("Promedio:", promedio)
print("Máximo:", maximo)
print("Mínimo:", minimo)
