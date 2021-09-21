



import numpy as np 
import random as rd 


class Jugador:

    mano = list()
    #constructor de la clase jugador
    def __init__(self,nombre, mano,tipo):
        self.nombre = nombre
        self.mano = mano 
        self.tipo = tipo

    #método que me muestra la mano que tiene el jugador
    def mostrarMano(self,numerada = False):
        i = 1
        for carta in self.mano:
            print((str(i) if numerada else "")+ (carta.getColor() if carta.getColor()!="NEGRO" else "")+ carta.getValor())

    def getTipo(self):
        return self.tipo
    
    def getNombre(self):
        return self.nombre


    #método para que el jugador seleccione una carta




class Juego:

    def __init__(self):
        self.monto = list()
        self.baraja = list()
        self.colores = ["NEGRO","ROJO","AMARILLO","AZUL","VERDE"]
        


    def crearBaraja(self):
        
        for valor in range(10):
            for color in self.colores[1:]:
                for _ in range(2 if valor > 0 else 1):
                    self.baraja.append(Carta(color,valor,"normal"))
        
        
        
        for valor in range(4):
            baraja.append(Carta())

 



class Carta:

    color = ""
    valor = ""
    tipo = ""

    def __init__(self, color, valor, tipo):
        self.color = color
        self.valor = valor
        self.tipo = tipo

    def getColor(self):

        return self.color

    def getValor(self):
        return self.valor


    def getTipo(self):
        return self.tipo
    
