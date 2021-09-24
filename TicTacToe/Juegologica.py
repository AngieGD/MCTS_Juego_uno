<<<<<<< HEAD
class Tablero():
    def __init__(self):
        self.tablero = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']]
        self.player = 'X'
        self.cpu = 'O'

    def imprimirTablero(self):
        print('-------------')
        cadena = ''
        for i in range(3):
            for j in range(3):
                cadena += "| " + self.tablero[i][j] + ' '
                if j == 2:
                    print(cadena + "|")
            cadena = ''
            if i == 2:
                print("-------------")

    def getTablero(self):
        return self.tablero

    def turnoJugador(self):
        print("Ingresa una posición dentro del tabler (1-9)")
        fila = 0
        col = 0
        while True:
            jugada = int(input())
            # Buscar la fila de la jugada
            if jugada >= 1 and jugada <= 9:
                if jugada % 3 == 0:
                    fila = jugada / 3
                else:
                    fila = int(jugada / 3) + 1
                # Buscar la columna de la jugada
                col = jugada - 3 * (fila - 1)
                # Se mira que la posición si sea valida
                #print("Bandera juagdor", fila, col)
                if self.tablero[int(fila-1)][int(col-1)] != '-':
                    print("Jugada invalida, ya hay una marca aqui")
                    continue
                else:
                    break
            else:
                print("La entrada es incorrecta, intente de nuevo")
                continue
        self.tablero[int(fila-1)][int(col-1)] = self.player
        self.imprimirTablero()

    def __str__(self):
        cadena = '-------------\n'
        for i in range(1, 4):
            for j in range(1, 4):
                cadena += "| " + self.tablero[i][j] + ' '
                if j == 3:
                    cadena += "|\n"
            cadena += ''
            if i == 3:
                cadena += "-------------"
        return cadena


class Juego:
    def __init__(self, t1,t2,t3,t4,t5,t6,t7,t8,t9):
        self.sTablero = [[t1.getTablero(), t2.getTablero(), t3.getTablero()],
                         [t4.getTablero(), t5.getTablero(), t6.getTablero()],
                         [t7.getTablero(), t8.getTablero(), t9.getTablero()]]

    def imprimirSuperTablero(self):
        # print('-------------')
        cadena = []
        rep = 0
        for row in range(0, 3):
            for col in range(0, 3):
                subTablero = self.sTablero[row][col]
                for fila in subTablero:
                    cadena.append(fila)

        cadena2 = [
            [cadena[0], cadena[9], cadena[18]],
            [cadena[1], cadena[10], cadena[19]],
            [cadena[2], cadena[11], cadena[20]],
            [cadena[3], cadena[12], cadena[21]],
            [cadena[4], cadena[13], cadena[22]],
            [cadena[5], cadena[14], cadena[23]],
            [cadena[6], cadena[15], cadena[24]],
            [cadena[7], cadena[16], cadena[25]],
            [cadena[8], cadena[17], cadena[26]]
        ]
        con = 0
        print('---------------------------------------------------') 
        for i in cadena2:
            print(i)
            con+=1
            if con % 3 == 0:
                print('---------------------------------------------------') 





tablero1= Tablero()
tablero2= Tablero()
tablero3= Tablero()
tablero4= Tablero()
tablero5= Tablero()
tablero6= Tablero()
tablero7= Tablero()
tablero8= Tablero()
tablero9= Tablero()
juego = Juego(tablero1,tablero2,tablero3,tablero4,tablero5,tablero6,tablero7,tablero8,tablero9)
juego.imprimirSuperTablero()

=======

import numpy as np
import pandas as pd 


class Table:

    def __init__(self):
        self.table = [['','',''],
                      ['','',''],
                      ['','','']]
        
        


    #método que me retorna los movimientos
    def getMoves(self):
        moves = []
        for x in range(self.table.shape[0]):
            for y in range(self.table.shape[1]):
                moves.append((x,y))


        return moves

    
def crearTablero():
    tablero_grande = np.zeros((3,3)).astype('object')

    for row in range(tablero_grande.shape[0]):
        for col in range(tablero_grande.shape[1]):
            tablero_grande[row,col] = Table()
    return tablero_grande


tablero = crearTablero()

def imprimirTablero(tablero):
    salida = ""
    matriz = ""
    for fila in tablero:
        for i in range(3):
            for table in fila:
                salida += repr(table.table[i])+" "
            matriz+=salida+"\n"
            salida = ""
        matriz+="\n"
    print(matriz)

imprimirTablero(tablero)

ganar = False


    





 
>>>>>>> master
