import numpy as np
import copy
from mcts import MonteCarloTreeSearchNode
from state import State
#from TicTacToe.mcts import MonteCarloTreeSearchNode

# Se definen las marcas de cada jugador
# Tomaremos al jugador1 con minmax y al jugador2 con MCTS
jugador1, jugador2 = 'X', 'O'


class Table:

    def __init__(self):
        self.table = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]

    # método que me retorna los movimientos
    def getMoves(self):
        moves = []
        for x in range(3):
            for y in range(3):
                if self.table[x][y] == ' ':
                    moves.append((x, y))

        return moves

    def insertarMarca(self, pos, marca):
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

    tablero_grande = np.zeros((3, 3)).astype('object')

    # creo una matriz de 3x3 donde voy a almacenar una instancia

    for row in range(tablero_grande.shape[0]):
        for col in range(tablero_grande.shape[1]):
            tablero_grande[row, col] = Table()
    return tablero_grande


tablero = crearTablero()


def imprimirTablero(tablero):
    salida = ""
    matriz = ""
    for fila in tablero:
        for i in range(3):
            for table in fila:
                salida += repr(table.table[i])+" "
            matriz += salida+"\n"
            salida = ""
        matriz += "\n"
    print(matriz)


def mostrarSubtablero(tablero):
    print("\nEl tablero es")
    table = tablero.table  # me devuelve una lista
    salida = ""
    for fila in table:
        salida += repr(fila) + '\n'

    print(salida)

# método para obtener la victoria

    # condicional ternario


def obtenerTablero(numero_tablero, tablero):

    i = 0

    for row in range(tablero.shape[0]):
        for column in range(tablero.shape[1]):

            if(i == numero_tablero-1):

                return tablero[row, column], (row, column)
            i += 1

    return None


def validarMovimiento(move, subtablero):
    moves = subtablero.getMoves()
    if move in moves:
        return True
    return False

# Implementacuón del MinMax

# Esta función evalua un arbol generado apartir de un estado de tablero


def minmax(tablero, profundidad, isMax):
    score = 10 if tablero.victoriaJugador(jugador1) else -10

    # Si gano el jugador
    if score == 10:
        return score
    # Si gano el contrincante
    if score == -10:
        return score
    # Averiguar si aun quedan movimientos
    moves = tablero.getMoves()
    if len(moves) == 0:
        return 0

    if isMax:
        best = -1000
        for i in moves:
            tablero.table[i[0]][i[1]] = jugador1
            # Se elije el valor maximo del arbol generado
            best = max(best, minmax(tablero, profundidad + 1, not isMax))
            tablero.table[i[0]][i[1]] = ' '
        return best
    else:
        best = 1000
        for i in moves:
            tablero.table[i[0]][i[1]] = jugador2
            # Se elije el valor minimo del arbol generado
            best = min(best, minmax(tablero, profundidad + 1, not isMax))
            tablero.table[i[0]][i[1]] = ' '

        return best


def minMaxMejorJugada(tablero, moves):
    bestVal = -1000
    bestMove = (-1, -1)
    for i in moves:
        tablero.table[i[0]][i[1]] = jugador1
        moveVal = minmax(tablero, 0, False)
        tablero.table[i[0]][i[1]] = ' '
        if (moveVal > bestVal):
            bestMove = (i[0], i[1])
            bestVal = moveVal
    return bestMove


def juegoPlayerVsMaquina():
    primerTurno = True
    # vamos a hacer el mejor videoJuego de la pinche historia
    gano = False

    jugadores = [{'nombre': 'Jugador1', 'movimientos': [], 'marca':jugador1}, {
        'nombre': 'Jugador2', 'movimientos': [], 'marca':jugador2}]

    while not gano:
        # primero mostramos el tablero

        # el turno de cada jugador
        for jugador in jugadores:

            imprimirTablero(tablero)
            #MonteCarloTreeSearchNode
            if primerTurno:
                opcion = int(input('Seleccione el tablero: (1:9): '))

                while ((opcion-1 < 0) or (opcion-1 > 9)):
                    print('\nPor favor, digite una opción entre (1:9)')
                    opcion = int(input('Seleccione el tablero: (1:9)'))
                subtablero, posicion = obtenerTablero(opcion, tablero)
                primerTurno = False

            print('\n')
            print('Turno del jugador: ', jugador['nombre'])
            print('Tablero: ', posicion)
            mostrarSubtablero(subtablero)
            sub = copy.copy(subtablero)
            if jugador['marca'] == jugador1:
                #TODO Traer la jugada usando MCTS
                print('\nSeleccione el movimiento que desea realizar: ')
                print(subtablero.getMoves())

                coordenada = input('\nDigite la coordenada (x,y): ')
                pos = coordenada.split(' ')
                pos = (int(pos[0]), int(pos[1]))

                while not validarMovimiento(pos, subtablero):
                    print('\nError, por favor digite un movimiento disponible')
                    coordenada = input('\nDigite la coordenada (x,y): ')
                    pos = coordenada.split(' ')
                    pos = (int(pos[0]), int(pos[1]))
            else:
                pos = minMaxMejorJugada(subtablero, subtablero.getMoves())

            # inserta los movimientos del jugador
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
            # el tablero obligatorio para el siguiente turno
            subtablero = tablero[(posicion)]

juegoPlayerVsMaquina()