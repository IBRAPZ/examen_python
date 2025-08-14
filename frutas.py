# NUNMERO 2

frutas = []

for i in range(5):
    fruta = input("Escribe una fruta: ")
    frutas.append(fruta)

frutas.sort()

print("Frutas ordenadas:")
for fruta in frutas:
    print(fruta)

# le pedi a la IA que me dijera como se guarda en un archivo txt 
with open("frutas.txt", "w") as archivo:
    for fruta in frutas:
        archivo.write(fruta + " ")
