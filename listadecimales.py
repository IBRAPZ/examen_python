#  NUMERO 6

numeros = []
for i in range(5):
    num = float(input(f"Ingrese el número decimal {i+1}: "))
    numeros.append(num)


promedio = sum(numeros) / len(numeros)
mayor = max(numeros)
menor = min(numeros)

print(f"Promedio: {promedio}")
print(f"Número mayor: {mayor}")
print(f"Número menor: {menor}")


ordenada = sorted(numeros)
print(f"Lista ordenada de menor a mayor: {ordenada}")
