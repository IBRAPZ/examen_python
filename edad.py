# NUMERO 1

def clasificar_edad(edad: int) -> str:
    if edad < 0:
        return "Edad no válida"
    elif edad < 12:
        return "Niño"
    elif 12 <= edad <= 17:
        return "Adolescente"
    elif 18 <= edad <= 64:
        return "Adulto"
    else:
        return "Adulto mayor"

# Solicita la edad al usuario (sin manejo de errores)
edad_usuario = int(input("Ingrese su edad: "))
resultado = clasificar_edad(edad_usuario)
print(f"Clasificación: {resultado}")

