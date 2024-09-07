from random import randint

# Solicitar el nombre del usuario
nombre = input("Ingrese su Nombre Por Favor: ")

# Informar al usuario sobre el juego
print(f"\tBueno, {nombre}, he pensado un número entre el 1 y 100 y tienes 8 intentos \n\tpara adivinar cuál crees que es el número.")

# Generar el número secreto
numeroelegido = randint(1, 100)

# Inicializar el número de intentos
numero = 0

# Bucle para los intentos
for intentos in range(1, 9):
    # Intentar convertir la entrada del usuario a un número entero
    try:
        numero = int(input(f"Ingresa el {intentos}° intento: \n"))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue  # Continuar con el siguiente intento si la entrada no es un número válido

    # Verificar si el número está fuera del rango permitido
    if (numero < 1) or (numero > 100):
        print("El número que has elegido no está permitido. Debe estar entre 1 y 100.")
    elif numero < numeroelegido:
        print(f"El {numero} es menor al número secreto.")
    elif numero > numeroelegido:
        print(f"El {numero} es mayor al número secreto.")
    else:
        print(f"¡Has acertado! El número secreto era {numeroelegido} y te tomó solo {intentos} intentos.")
        break
else:
    # Este bloque se ejecuta si el bucle no se rompe con un 'break'
    print(f"Lo siento, se han agotado los intentos. El número secreto era {numeroelegido}.")
