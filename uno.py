import numpy as np 
import random as rd
import pandas as pd



monto = []
baraja = []

def crearBaraja():

    colores = ["NEGRO","AZUL","VERDE","ROJO","AMARILLO"]
    baraja = []
    
    #crear baraja de cartas
    for value in range(10):
        #solo toma los colores 
        for color in colores[1:]:
            #esta instrucción se me repite 2 veces
            for _ in range(2 if value >0 else 1):
                baraja.append({"color":color,"valor":str(value)})
        
    #este for significa que no me importa el valor de i para no gastar memoria
    for _ in range(4):
        baraja.append({"color":"NEGRO", "valor":"+4"})
        baraja.append({"color":"NEGRO", "valor":"COMODIN"})


    for color in colores[1:]:
        for _ in range(2):
            baraja.append({"color":color, "valor":"+2"})
            baraja.append({"color":color, "valor":"CAMBIO"})
            baraja.append({"color":color, "valor":"OMITIR"})

    rd.shuffle(baraja)
    return baraja



baraja = crearBaraja()

##
jugadores = [{"nombre":"", "mano":[],"tipo":"normal"}, {"nombre":"robot", "mano":[],"tipo":"AI"}]
##pido el nombre del jugador
jugadores[0]["nombre"] = "Eduardo"


for _ in range(7):
    for jugador in jugadores:
        jugador["mano"].append(baraja[0])
        baraja = baraja[1:]



#en esta etapa el jugador ya tiene una baraja de 7 cartas con respecto a las otras
""" for jugador in jugadores:
    print("\n")
    print(jugador["nombre"])
    print("\nMANO")

    for carta in jugador["mano"]:
        print( ( carta["color"]+" " if carta["color"]!="NEGRO" else "") + carta["valor"] )
 """

def pintarCarta(carta):
    return ( carta["color"]+" " if carta["color"]!="NEGRO" else "") + carta["valor"] 


def mostrarMano(jugador, enumerada = False):
    i = 1
    for carta in jugador["mano"]:
        print( (str(i) if enumerada else "")+ ( carta["color"] + " " if carta["color"]!="NEGRO" else "") + carta["valor"]  )
        i+=1

#me retorna un booleano
def validarCarta(carta, carta_mesa):
    pass


def escogerCarta(jugador, monto, baraja):

    repetir = True
    while repetir:
        mostrarMano(jugador, True)
        print("\r\n\rCarta en la mesa: ", pintarCarta(monto[-1]))
        carta = input("Qué carta quieres escoger? r(robar)")

        if (carta.upper() == "R"):
            ## en caso en el que el jugador decida robar una carta
            if len(baraja)>=0:
                jugador["mano"].append(baraja[0])
                baraja = baraja[1:]



    return monto, baraja

        

    



monto.append(baraja[0])
baraja = baraja[1:]

continuar = True

while continuar:

    if(len(baraja)) <= 0:
        continuar = False 

    for jugador in jugadores:
        print("Turno de "+jugador["nombre"])
        

        mostrarMano(jugador)
        

        continuar = False


    



