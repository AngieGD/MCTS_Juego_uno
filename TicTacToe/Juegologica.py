
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
        self.table = np.array([['','',''],
                               ['','',''],
                               ['','','']])

    def getTable(self):
        return self.table

    #método que me retorna los movimientos
    def getMoves(self):
        
        pass


tablero = Table()


tablero_grande = np.zeros((3,3)).astype('object')

for row in range(tablero_grande.shape[0]):
    for col in range(tablero_grande.shape[1]):
        tablero_grande[row,col] = Table()








""" 
jugadores = [{'nombre':'Eduardo', 'escogido':''}, {'nombre':'Bot', 'escogido':''}]

for jugador in jugadores:
    print(jugador)



 """