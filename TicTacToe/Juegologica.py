
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


    





 