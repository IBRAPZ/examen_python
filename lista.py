# NUMERO 5

numeros = [12, 45, 67, 89, 23, 56, 78, 34, 90, 11]

print("Todos los números:")
for numero in numeros:
    print(numero)

print("Números mayores que 50:")
for numero in numeros:
    if numero > 50:
        print(numero)

#le pedi ayuda a la IA para el append y extend (no me acordaba como se usaban)
numeros.append(99.9)
numeros.extend([88.8])

numeros.insert(3, 100.5)

numeros.remove(numeros[0])  # elimina el primer valor
numeros.pop()               # elimin el último elemento

print("Lista final:")
print(numeros)
print(f"Cantidad de elementos: {len(numeros)}")
