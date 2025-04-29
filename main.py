#importacion de campeones
from campeones.camille import camille
from campeones.lux import lux
from campeones.thresh import thresh

#importacion de objetos
from objetos.botas import botas
from objetos.espada import espada

#importacion de menu
from utilidades.menu import menu
from utilidades.menu import champ
from utilidades.menu import equipamiento

bandera = True #lo usamos para entrar en el bucle

while bandera:

    opcion_champ = champ() # almacenamos el valor retornado de la funcion
    opcion_menu = menu() # almacenamos el valor retornado de la funcion

    if opcion_champ == 1: 
        #camille
        print("Has elegido a Camille")
        if opcion_menu == 1:
            camille()
        elif opcion_menu == 2:
            print("Camille se vuelve intargetiable por 0.5 segundos, y salta hasta el champ tarjeteado logrando asi encerrarlo en un hexagono perfecto por 2,5 segundos")
        elif opcion_menu == 3:
            equip = equipamiento() # almacenamos el valor retornado de la funcion
            if equip == 1:
                espada(68)
            elif equip == 2:
                botas(350)
            elif equip == 3:
                print ("Volviendo al menu...")
        elif opcion_menu == 4:
            print("saliendo del programa...")
            bandera = False # salimos del bucle while
        else:
            print ("algo salio mal")

    elif opcion_champ == 2: 
        #thresh
        print("Has elegido a Thresh")
        if opcion_menu == 1:
            thresh()
        elif opcion_menu == 2:
            print("Thresh crea un pentagono a su alrededor (5s) de alma que realentiza a todo aquel que lo atraviese")
        elif opcion_menu == 3:
            equip = equipamiento() # almacenamos el valor retornado de la funcion
            if equip == 1:
                espada(56)
            elif equip == 2:
                botas(330)
            elif equip == 3:
                print ("Volviendo al menu...")
        elif opcion_menu == 4:
            print("saliendo del programa...")
            bandera = False # salimos del bucle while 

    elif opcion_champ == 3: 
        #lux
        print("Has elegido a Lux")
        if opcion_menu == 1:
            lux()
        elif opcion_menu == 2:
            print("Lux crea un rayo de luz hacia adelante que hace daño magico a todos los enemigos que lo atraviesen.")
        elif opcion_menu == 3:
            equip = equipamiento() # almacenamos el valor retornado de la funcion
            if equip == 1:
                espada(54)
            elif equip == 2:
                botas(330)
            elif equip == 3:
                print ("Volviendo al menu...")
        elif opcion_menu == 4:
            print("saliendo del programa...")
            bandera = False # salimos del bucle while
    else:
        print ("algo terriblemente salio mal")