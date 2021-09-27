import numpy as np
import pandas as pd 


class Table:

    def __init__(self):
        self.table = [[' ',' ',' '],
                      [' ',' ',' '],
                      [' ',' ',' ']]
        
    #método que me retorna los movimientos
    def getMoves(self):
        moves = []
        for x in range(3):
            for y in range(3):
                if self.table[x][y] ==' ':
                    moves.append((x,y))


        return moves

    def insertarMarca(self,pos,marca):
        self.table[pos[0]][pos[1]] = marca


    def victoriaJugador(self, marca):
        
        for i in range(3):
            # Comprobación de filas
            if (self.table[i][0] == marca and self.table[i][1] == marca and self.table[i][2] == marca):
                return True
            else:
                    # Comprobación de Columnas
                if (self.table[0][i] == marca and self.table[1][i] == marca and self.table[2][i] == marca):
                    return True
            # Comprobacion de diagonales
            # Diagonal Principal
            if (self.table[0][0] == marca and self.table[1][1] == marca and self.table[2][2] == marca):
                return True
            # Diagonal secundaria
            if (self.table[0][2] == marca and self.table[1][1] == marca and self.table[2][0] == marca):
                return True

        return False


    
def crearTablero():
    
    tablero_grande = np.zeros((3,3)).astype('object')

    #creo una matriz de 3x3 donde voy a almacenar una instancia

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


def mostrarSubtablero(tablero):
    print("\nEl tablero es")
    table = tablero.table #me devuelve una lista
    salida = ""
    for fila in table:
        salida+=repr(fila) + '\n'

    print(salida)

#método para obtener la victoria

        #condicional ternario 
def obtenerTablero(numero_tablero, tablero):

    i = 0

    for row in range(tablero.shape[0]):
        for column in range(tablero.shape[1]):
            
            if(i == numero_tablero-1):

                return tablero[row,column], (row,column)
            i+=1

    return None    

def validarMovimiento(move, subtablero):
    moves = subtablero.getMoves()
    if move in moves:
        return True 
    return False
    


jugadores = [{'nombre':'Eduardo', 'movimientos':[],'marca':'X'},{'nombre':'bot', 'movimientos':[],'marca':'O'}]

primerTurno = True
#vamos a hacer el mejor videoJuego de la pinche historia
gano = False

while not gano:
    #primero mostramos el tablero
    
    #el turno de cada jugador
    for jugador in jugadores:

        imprimirTablero(tablero)
        
        if primerTurno:
            opcion = int(input('Seleccione el tablero: (1:9): '))

            while ((opcion-1 < 0) or (opcion-1 >9 ) ):
                print('\nPor favor, digite una opción entre (1:9)')
                opcion = int(input('Seleccione el tablero: (1:9)'))
            subtablero, posicion = obtenerTablero(opcion,tablero)
            primerTurno = False

        print('\n')
        print('Turno del jugador: ', jugador['nombre'])
        print('Tablero: ', posicion)
        mostrarSubtablero(subtablero)
        print('\nSeleccione el movimiento que desea realizar: ')
        print(subtablero.getMoves())

        coordenada = input('\nDigite la coordenada (x,y): ')
        pos = coordenada.split(' ')
        pos = (int(pos[0]), int(pos[1]))

        while not validarMovimiento(pos,subtablero):
            print('\nError, por favor digite un movimiento disponible')
            coordenada = input('\nDigite la coordenada (x,y): ')
            pos = coordenada.split(' ')
            pos = (int(pos[0]), int(pos[1]))

        #inserta los movimientos del jugador
        jugador['movimientos'].append(pos)

        subtablero.insertarMarca(pos, jugador['marca'])

        mostrarSubtablero(subtablero)
        
        if subtablero.victoriaJugador(jugador['marca']):
            
            ganador = jugador['nombre']
            movimientos = jugador['movimientos']
            tablero_ganador = subtablero.table

            gano = True  
            break          



        tablero[posicion] = subtablero

        posicion = pos
        subtablero = tablero[posicion] #el tablero obligatorio para el siguiente turno






        



        

            











    

    








