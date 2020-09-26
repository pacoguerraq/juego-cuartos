import time

casa = [["cuarto niños", "biblioteca", "cuarto papás"],
        ["salón de juegos", "comedor", "cocina"],
        ["baño", "lobby", "sala"]]

print("\nBIENVENIDO AL JUEGO")
time.sleep(1)
print("-- Estás en el centro de la casa, recolecta las 3 monedas y sal para ganar")
time.sleep(1)
print("-- Debes moverte entre cuartos para encontrar monedas (\"fwd\" para adelante, \"back\" para atrás, \"der\" para la derecha y \"izq\" para la izquierda)")
time.sleep(1)
print("-- Si entras a un cuarto con trampa, mueres")
time.sleep(1)
print("-- TIENES 3 VIDAS\n")
# print("-- Para ver cuantas monedas tienes escribe \'coins\'")
row = 1
column = 1


def movimiento(row, column):
    coins = 0
    sala, cocina, cuarto_ninos, salon_juegos, cuarto_papas, bano = 0, 0, 0, 0, 0, 0
    vidas = 3
    nueva_vida = 3
    while not (((casa[row][column]) == "lobby") and (coins == 3)):
        if nueva_vida != vidas:
            vidas = vidas - 1
            if vidas == 0:
                print("-------------------")
                print("-- LO SIENTO, NO TE QUEDAN VIDAS Y HAZ PERDIDO, VUELVE PRONTO")
                exit()
            else:
                print("-- Se quitará la trampa y reiniciará el juego.")
                print("-- Te quedan", vidas, "vidas")
        if coins == 3:
            print("-------------------")
            print("-- Tienes todas las monedas, ahora dirígete a la salida (lobby)")
        else:
            print("-------------------")
            print("-- Tienes", coins, "moneda(s), te faltan", (3 - coins))

        posicion = casa[row][column]
        print("-- Estás en " + posicion)
        direccion = input(
            "** A donde quieres ir?: ")
        if direccion == "der":
            if (column + 1) < 3:
                column = column + 1
            else:
                print("-- Hay una pared, no puedes dirigirte en esa dirección.")
        elif direccion == "izq":
            if (column - 1) < 0:
                print("-- Hay una pared, no puedes dirigirte en esa dirección.")
            else:
                column = column - 1
        elif direccion == "fwd":
            if (row - 1) < 0:
                print("-- Hay una pared, no puedes dirigirte en esa dirección.")
            else:
                row = row - 1
        elif direccion == "back":
            if (row + 1) > 2:
                print("-- Hay una pared, no puedes dirigirte en esa dirección.")
            else:
                row = row + 1
        else:
            print("-- Escribe una dirección válida")

        if ((casa[row][column]) == "sala"):
            if sala == 0:
                sala = 1
                coins = coins + 1
                print("-- BIEN, recogiste una moneda")
            else:
                print("-- Ya recogiste la moneda de este cuarto")
        elif ((casa[row][column]) == "cocina"):
            if cocina == 0:
                cocina = 1
                coins = coins + 1
                print("-- BIEN, recogiste una moneda")
            else:
                print("-- Ya recogiste la moneda de este cuarto")
        elif ((casa[row][column]) == "cuarto niños"):
            if cuarto_ninos == 0:
                cuarto_ninos = 1
                coins = coins + 1
                print("-- BIEN, recogiste una moneda")
            else:
                print("-- Ya recogiste la moneda de este cuarto")

        if ((casa[row][column]) == "salón de juegos"):
            if salon_juegos == 0:
                print(
                    "-- OH NO! Haz caído en la trampa de este cuarto y moriste.")
                row = 1
                column = 1
                salon_juegos = salon_juegos + 1
                nueva_vida = vidas - 1
            else:
                print(
                    "-- Te salvaste, la trampa de este cuarto se removió en un juego pasado.")
        elif ((casa[row][column]) == "baño"):
            if bano == 0:
                print(
                    "-- OH NO! Haz caído en la trampa de eset cuarto y moriste.")
                row = 1
                column = 1
                bano = bano + 1
                nueva_vida = vidas - 1
            else:
                print(
                    "-- Te salvaste, la trampa de este cuarto se removió en un juego pasado.")
        elif ((casa[row][column]) == "cuarto papás"):
            if cuarto_papas == 0:
                print(
                    "-- OH NO! Haz caído en la trampa de eset cuarto y moriste.")
                row = 1
                column = 1
                cuarto_papas = cuarto_papas + 1
                nueva_vida = vidas - 1
            else:
                print(
                    "-- Te salvaste, la trampa de este cuarto se removió en un juego pasado.")

    if (sala == 1) and (cuarto_ninos == 1) and (cocina == 1):
        print("¡FELICIDADES, saliste con las 3 monedas!")


movimiento(row, column)
