# NUMERO 7 
mi_tupla = (5, 10, 15, 20, 25, 30)


mi_lista = list(mi_tupla)
mi_lista.append(99.9)
mi_tupla_modificada = tuple(mi_lista)


print(f"Tupla modificada: {mi_tupla_modificada}")
print(f"Valor en la posición 4: {mi_tupla_modificada[4]}")
print(f"Total de elementos: {len(mi_tupla_modificada)}")
