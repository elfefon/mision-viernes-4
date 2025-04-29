def menu():

    opciones = 0  # inicializamos opciones

    while opciones != 4:
        print("\n--- Menú de Opciones --- \n1. Mostrar atributos del campeón \n2. Usar habilidad definitiva \n3. Equipar objeto y mostrar estadísticas \n4. Salir \n")

        opcion_input = input("\nIngrese una opción: ")

        if opcion_input.isdigit():  # validamos que sea numero
            opciones = int(opcion_input)
            if 1 <= opciones <= 4:
                return opciones  # retornamos la opcion elegida como int
            else:
                print("Por favor ingrese un número entre 1 y 4.")
        else:
            print("Entrada inválida. Ingrese un número.")


def champ():

    bandera = True # entramos al bucle while

    while bandera: 
        print ("Elige un champ: \n1. Camille \n2. Thresh \n3. Lux \n")

        champ_input = input ("Ingrese un numero: ")

        if champ_input.isdigit(): 
            champ_input = int (champ_input)
            if 1 <= champ_input <= 3:
                return champ_input # retornamos el campeon elegido como int
        else:
            print("ingrese un valor valido")


def equipamiento():

    input_equipamiento = 0 # inicializamos 

    while input_equipamiento != 3:
        print ("¿Que quieres equiparle?")
        print ("1. Espada \n2. Botas \n3. Salir")

        input_equipamiento = input ("ingresa una de las tres opciones en formato de numero: ") 

        if input_equipamiento.isdigit():
            input_equipamiento = int (input_equipamiento)
            if 1 <= input_equipamiento <= 3:
                return input_equipamiento
            else:
                print("Ingrese un numero valido.")
        else:
            print("Entrada invalida. Ingrese un numero")