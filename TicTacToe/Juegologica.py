
import numpy as np
import pandas as pd 

""" 

#creación del tablero vacío
table = np.array([ [[ ['','',''],
                     ['','',''],
                     ['','',''] ],
                     [ ['','',''],
                     ['','',''],
                     ['','',''] ],
                     [ ['','',''],
                     ['','',''],
                     ['','',''] ] ],
                     [[ ['','',''],
                     ['','',''],
                     ['','',''] ],
                     [ ['','',''],
                     ['','',''],
                     ['','',''] ],
                     [ ['','',''],
                     ['','',''],
                     ['','',''] ] ],
                     [[ ['','',''],
                     ['','',''],
                     ['','',''] ],
                     [ ['','',''],
                     ['','',''],
                     ['','',''] ],
                     [ ['','',''],
                     ['','',''],
                     ['','',''] ] ]
                ])


print(table.shape) """

class Table:

    def __init__(self):
        self.table = [[1,2,3],
                      [4,5,6],
                      [7,8,9]]
        
        


    #método que me retorna los movimientos
    def getMoves(self):
        moves = []
        for x in range(self.table.shape[0]):
            for y in range(self.table.shape[1]):
                moves.append((x,y))


        return moves

    




tablero = Table()


tablero_grande = np.zeros((3,3)).astype('object')

for row in range(tablero_grande.shape[0]):
    for col in range(tablero_grande.shape[1]):
        tablero_grande[row,col] = Table()


def imprimirTablero(superTablero):

    salida = ""
    matriz = ""
    for fila in superTablero:
        for table in fila:
            #primera matriz
            for row in table.table:
                for col in row:
                    salida+=str(col) +'|' 
                salida+="\n" #1 fila 
            matriz += salida
            #matriz = salida
            salida = ""    
        matriz+="\n" 
    print(matriz)
    


imprimirTablero(tablero_grande)

""" 
jugadores = [{'nombre':'Eduardo', 'escogido':''}, {'nombre':'Bot', 'escogido':''}]

for jugador in jugadores:
    print(jugador)



 """


 