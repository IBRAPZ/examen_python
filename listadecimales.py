#  NUMERO 6

numeros = []
for i in range(5):
    num = float(input(f"Ingrese el número decimal {i+1}: "))
    numeros.append(num)

# 6.1. Calcula y muestra
promedio = sum(numeros) / len(numeros)
mayor = max(numeros)
menor = min(numeros)

print(f"Promedio: {promedio}")
print(f"Número mayor: {mayor}")
print(f"Número menor: {menor}")

# 6.2. Ordena la lista de menor a mayor sin usar sort() directamente
ordenada = sorted(numeros)
print(f"Lista ordenada de menor a mayor: {ordenada}")
