# NUMERO 8

inventario = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del producto {i+1}: ")
    precio = float(input(f"Ingrese el precio de '{nombre}': "))
    cantidad = int(input(f"Ingrese la cantidad de '{nombre}': "))
    inventario[nombre] = (precio, cantidad)

print("Inventario:")
for producto, (precio, cantidad) in inventario.items():
    print(f"- {producto}: Precio = ${precio:.2f}, Cantidad = {cantidad}")

valor_total = sum(precio * cantidad for precio, cantidad in inventario.values())
print(f" Valor total del inventario: ${valor_total:.2f}")
