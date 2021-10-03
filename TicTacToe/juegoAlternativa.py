
import numpy as np
import pandas as pd

from os import system


class Table():

    def __init__(self):
        self.table = [[' ',' ',' '],
                      [' ',' ',' '],
                      [' ',' ',' ']]

    def getMoves(self):
        moves = []

        for x in range(3):
            for y in range(3):
                if self.table[x][y] == ' ':
                    moves.append((x,y))
        return moves

    def insertarMarca(self,pos,marca):
        #método para insertar una marca
        self.table[pos[0]][pos[1]] = marca

    #función que me muestra el tablero
    def mostrarTablero(self):
        salida = ""
        for fila in self.table:
            salida+= repr(fila)+"\n"
        print(salida)


class SuperTable():


    tablero = np.zeros((3,3)).astype('object')

    def __init__(self):
        self.crearTablero()

    
    def crearTablero(self):
    
        for row in range(self.tablero.shape[0]):
            for column in range(self.tablero.shape[1]):
                self.tablero[row,column] = Table()
    
    def mostrarTablero(self):
        salida = ""
        matriz = ""
        for fila in self.tablero:
            for i in range(3):
                for tablero in fila:
                    salida += repr(tablero.table[i])+" "
                matriz+=salida+"\n"
                salida = ""
            matriz+="\n"
        
        print(matriz)

    def numeroMovimientos(self):
        count = 0 
        for fila in self.tablero:
            for table in fila:
                count+=len(table.getMoves())

        return count


#método para obtener la posición
def obtenerTablero(opcion, tablero):
    i = 0
    for row in range(tablero.tablero.shape[0]):
        for column in range(tablero.tablero.shape[1]):
            if i==opcion-1:
                return (row,column)
            i+=1
    
    return None

#método para validar la jugada

def validarJugada(pos, tablero):

    if pos in tablero.getMoves():
        return True 
    
    return False


def seleccionarMovimiento(pos, tablero, jugador):
    
    print("\nTablero: ", pos)
    #tablero.tablero[pos].mostrarTablero()
    print(tablero.tablero[pos].mostrarTablero())

    print('\nMovimientos disponibles: ', tablero.tablero[pos].getMoves())
    coordenada = input('Seleccione la el movimiento que desea realizar(x y): ')
    posicion = coordenada.split(' ')
    posicion = (int(posicion[0]), int(posicion[1])) #recibe la posicion

    while not validarJugada(pos, tablero.tablero[pos]):
        
        print('Por favor, digite un movimiento correspondiente')
        print('\nMovimientos disponibles: ', tablero[pos].getMoves())

        coordenada = input('Seleccione la el movimiento que desea realizar(x y): ')
        posicion = coordenada.split(' ')
        posicion = (int(posicion[0]), int(posicion[1])) #recibe la posicion

    tablero.tablero[pos].insertarMarca(posicion, jugador['marca'])


    return tablero, posicion
    


# implementación
def turnoJugador(jugador):
    pass

# implementación
def turnoMaquina(maquina):
    pass


if __name__ =='__main__':

    system('clear')

    #primero se crea un tablero
    tablero = SuperTable()
    tablero.mostrarTablero()

    print('Numero de movimientos: ',tablero.numeroMovimientos())
    jugadores = [{'nombre':'Eduardo','movimientos':[], 'marca':'X','tipo':'normal'},{'nombre':'bot','movimientos':[],'marca':'O','tipo':'IA'}]

    #generarTurnoAleatorio

    jugador = jugadores[np.random.randint(len(jugadores))]

    opcion = int(input('Seleccione un tablero(1:9): '))

    #valida la opción

    while (opcion-1 <0) or (opcion-1>8):

        print('Por favor, seleccione un tablero: ')  
        opcion = int(input('Seleccione un tablero(1:9): '))

    #posición del tablero 
    pos = obtenerTablero(opcion, tablero)
    tablero, pos = seleccionarMovimiento(pos, tablero, jugador)
    
    tablero.mostrarTablero()
    
    

