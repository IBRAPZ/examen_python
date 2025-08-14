# NUMERO 9 

lista = []

while True:
    print(" ¿Qué quiere hacer? ")
    print("1. Añadir un numero")
    print("2. Insertar un número en una posición específica")
    print("3. Eliminar un número por valor")
    print("4. Eliminar un número por índice")
    print("5. Mostrar la lista")
    print("6. Salir")

    opcion = input("Escribe el número de la opción: ")

    if opcion == "1":
        num = input("Ingresa el número que deseas añadir: ")
        try:
            lista.append(float(num))
            print("+Numero añadido.")
        except ValueError:
            print("no es numero válido.")

    elif opcion == "2":
        num = input("Numero a insertar: ")
        pos = input("Posición donde insertarlo: ")
        try:
            num = float(num)
            pos = int(pos)
            if 0 <= pos <= len(lista):
                lista.insert(pos, num)
                print(" Numero insertado.")
            else:
                print("Posición fuera de rango.")
        except ValueError:
            print("❌ Entrada inválida.")

    elif opcion == "3":
        num = input("Numero que deseas eliminar: ")
        try:
            num = float(num)
            if num in lista:
                lista.remove(num)
                print("Numero eliminado.")
            else:
                print(" Ese numero no está en la lista.")
        except ValueError:
            print("Entrada inválida.")

    elif opcion == "4":
        pos = input("indice que deseas eliminar: ")
        try:
            pos = int(pos)
            if 0 <= pos < len(lista):
                eliminado = lista.pop(pos)
                print(f" Numero {eliminado} eliminado.")
            else:
                print("indice fuera de rango.")
        except ValueError:
            print("Entrada invalida.")

    elif opcion == "5":
        print("Lista actual:", lista)

    elif opcion == "6":
        print("Hasta luego")
        break

    else:
        print("opcion no valida")
