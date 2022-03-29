import random
import numpy as np
salir = True
ocupado = True
juego = True
pasos = 0
punteo = 0
vacio = " "
jugador = "C"
iconoc = "@"
iconot = "#"
posiciones = [" ", " ", " ", " ", " ", " "]
contador = 0
punteos = [0, 0, 0, 0, 0, 0]
nombre = " "
prueba = 0
prueba1 = " "
while salir:
    print("PACMAN - IPC 1 - 2022")
    print("---------------------")
    print("1.      Iniciar juego")
    print("2.   Tabla Posiciones")
    print("3.              Salir")
    print("---------------------")
    print("Ingrese una opción...")
    opcion = int(input())
    if opcion == 1:
        pasos = 0
        punteo = 0
        print("Ingrese su nombre:")
        nombre = input()
        contador += 1
        tablero = np.array([[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]])
        po1 = random.randint(0, 9)
        po2 = random.randint(0, 9)
        tablero[po1][po2] = jugador
        comida = random.randint(8, 40)
        for i in range(0, comida):
            ocupado = True
            while ocupado:
                pos1 = random.randint(0, 9)
                pos2 = random.randint(0, 9)
                if tablero[pos1][pos2] == " ":
                    tablero[pos1][pos2] = iconoc
                    ocupado = False
        ocupado = True
        for i in range(0, 30):
            pos1 = random.randint(0, 9)
            pos2 = random.randint(0, 9)
            if tablero[pos1][pos2] == " ":
                tablero[pos1][pos2] = iconot
                ocupado = False
        for line in tablero:
            print("|", end="")
            print('  '.join(map(str, line)), end="")
            print("|")
        while juego and punteo < 40:
            print("Punteo: ", punteo, "    Pasos:", pasos)
            print("------------------------------------")
            for line in tablero:
                print("|", end="")
                print('  '.join(map(str, line)), end="")
                print("|")
            print("------------------------------------")
            print("Realice un movimiento:")
            mov = input()
            if (mov == "w" or mov == "8") and (po1 - 1) < 0 and tablero[9][po2] == vacio:
                tablero[po1][po2] = vacio
                po1 = 9
                tablero[po1][po2] = jugador
                pasos = pasos + 1
            elif (mov == "w" or mov == "8") and (po1 - 1) < 0 and tablero[9][po2] == iconoc:
                tablero[po1][po2] = vacio
                po1 = 9
                tablero[po1][po2] = jugador
                pasos = pasos + 1
                punteo += 5
            elif (mov == "w" or mov == "8") and (po1 - 1) < 0 and tablero[9][po2] == iconot:
                pasos = pasos + 1
            elif (mov == "w" or mov == "8") and tablero[po1-1][po2] == vacio:
                tablero[po1][po2] = vacio
                po1 = po1-1
                tablero[po1][po2] = jugador
                pasos = pasos + 1
            elif (mov == "w" or mov == "8") and tablero[po1-1][po2] == iconoc:
                tablero[po1][po2] = vacio
                po1 = po1-1
                tablero[po1][po2] = jugador
                punteo = punteo + 5
                pasos = pasos + 1
            elif (mov == "w" or mov == "8") and tablero[po1-1][po2] == iconot:
                pasos = pasos + 1
            elif (mov == "s" or mov == "2") and (po1+1)>9 and tablero[0][po2] == vacio:
                tablero[po1][po2] = vacio
                po1 = 0
                tablero[0][po2] = jugador
                pasos = pasos + 1
            elif (mov == "s" or mov == "2") and (po1+1)>9 and tablero[0][po2] == iconoc:
                tablero[po1][po2] = vacio
                po1 = 0
                tablero[po1][po2] = jugador
                punteo += 5
                pasos += 1
            elif (mov == "s" or mov == "2") and (po1+1)>9 and tablero[0][po2] == iconot:
                pasos +=1
            elif (mov == "s" or mov == "2") and tablero[po1+1][po2] == vacio:
                tablero[po1][po2] = vacio
                po1 = po1+1
                tablero[po1][po2] = jugador
                pasos = pasos + 1
            elif (mov == "s" or mov == "2") and tablero[po1+1][po2] == iconoc:
                tablero[po1][po2] = vacio
                po1 = po1 + 1
                tablero[po1][po2] = jugador
                pasos = pasos + 1
                punteo = punteo + 5
            elif (mov == "s" or mov == "2") and tablero[po1+1][po2] == iconot:
                pasos = pasos + 1
            elif (mov == "a" or mov == "4") and (po2-1) < 0 and tablero[po1][9] == vacio:
                tablero[po1][po2] = vacio
                po2 = 9
                tablero[po1][po2] = jugador
                pasos = pasos + 1
            elif (mov == "a" or mov == "4") and (po2-1) < 0 and tablero[po1][9] == iconoc:
                tablero[po1][po2] = vacio
                po2 = 9
                tablero[po1][po2] = jugador
                punteo += 5
                pasos += 1
            elif (mov == "a" or mov == "6") and (po2-1) < 0 and tablero[po1][po2] == iconot:
                pasos += 1
            elif (mov == "a" or mov == "4") and tablero[po1][po2-1] == vacio:
                tablero[po1][po2] = vacio
                po2 -= 1
                tablero[po1][po2] = jugador
                pasos += 1
            elif (mov == "a" or mov == "2") and tablero[po1][po2-1] == iconoc:
                tablero[po1][po2] = vacio
                po2 = po2 - 1
                tablero[po1][po2] = jugador
                punteo += 5
                pasos += 1
            elif (mov == "a" or mov == "4") and tablero[po1][po2-1] == iconot:
                pasos += 1
            elif (mov == "d" or mov == "6") and (po2+1) > 9 and tablero[po1][0] == vacio:
                tablero[po1][po2] = vacio
                po2 = 0
                tablero[po1][po2] = jugador
                pasos += 1
            elif (mov == "d" or mov == "6") and (po2+1) > 9 and tablero[po1][0] == iconoc:
                tablero[po1][po2] = vacio
                po2 = 0
                tablero[po1][po2] = jugador
                punteo += 5
                pasos += 1
            elif (mov == "d" or mov == "6") and (po2+1) > 9 and tablero[po1][0] == iconot:
                pasos += 1
            elif (mov == "d" or mov == "6") and tablero[po1][po2+1] == vacio:
                tablero[po1][po2] = vacio
                po2 += 1
                tablero[po1][po2] = jugador
                pasos += 1
            elif (mov == "d" or mov == "6") and tablero[po1][po2+1] == iconoc:
                tablero[po1][po2] = vacio
                po2 += 1
                tablero[po1][po2] = jugador
                punteo += 5
                pasos += 1
            elif (mov == "d" or mov == "6") and tablero[po1][po2+1] == iconot:
                pasos += 1
            elif mov == "e":
                juego = False
        juego = True
        print("El juego ha finalizado")
        print(nombre, "tu puntuación final es:", punteo)
    if opcion == 2:
        print("Todavía no está hecho, lo siento.")
        print("La tabla de posiciones es:")
        posiciones[contador] = nombre
        punteos[contador] = pasos
        for i in range(6):
            if punteos[5] > punteos[4]:
                prueba = punteos[4]
                punteos[4] = punteos[5]
                punteos[5] = prueba
                prueba1 = posiciones[4]
                posiciones[4] = posiciones[5]
                posiciones[5] = prueba1
            if punteos[4] > punteos[3]:
                prueba = punteos[3]
                punteos[3] = punteos[4]
                punteos[4] = prueba
                prueba1 = posiciones[3]
                posiciones[3] = posiciones[4]
                posiciones[4] = prueba1
            if punteos[3] > punteos[2]:
                prueba = punteos[2]
                punteos[2] = punteos[3]
                punteos[3] = prueba
                prueba1 = posiciones[2]
                posiciones[2] = posiciones[3]
                posiciones[3] = prueba1
            if punteos[2] > punteos[1]:
                prueba = punteos[1]
                punteos[1] = punteos[2]
                punteos[2] = prueba
                prueba1 = posiciones[1]
                posiciones[1] = posiciones[2]
                posiciones[2] = prueba1

        print("1.", posiciones[1], punteos[1])
        print("2.", posiciones[2], punteos[2])
        print("3.", posiciones[3], punteos[3])
        print("4.", posiciones[4], punteos[4])
        print("5.", posiciones[5], punteos[5])
    if opcion == 3:
        print("Gracias por jugar!")
        salir = False