import numpy as np
import copy
from minmax import minMaxMejorJugada
from mcts import MonteCarloTreeSearchNode
from state import State
#from TicTacToe.mcts import MonteCarloTreeSearchNode

# Se definen las marcas de cada jugador
# Tomaremos al jugador1 con minmax y al jugador2 con MCTS
jugador1, jugador2 = 'O', 'X'


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


def juegoMinMaxVSminMax():
    tablero = crearTablero()
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
                opcion = np.random.randint(1,10)
                subtablero, posicion = obtenerTablero(opcion, tablero)
                primerTurno = False

            print('\n')
            print('Turno del jugador: ', jugador['nombre'])
            print('Tablero: ', posicion)
            mostrarSubtablero(subtablero)
            sub = copy.deepcopy(subtablero)
            if jugador['marca'] == jugador1:
                if len(subtablero.getMoves()) == 9:
                    pos = subtablero.getMoves()[np.random.randint(1,9)]
                else:
                    pos = minMaxMejorJugada(subtablero, subtablero.getMoves())
            else:
                if len(subtablero.getMoves()) == 9:
                    pos = subtablero.getMoves()[np.random.randint(1,9)]
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
    imprimirTablero(tablero)
    print('El ganador es!!!: ', ganador)
    return ganador

def juegoMCTSvsMCTS():
    tablero = crearTablero()
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
                opcion = np.random.randint(1,10)
                subtablero, posicion = obtenerTablero(opcion, tablero)
                primerTurno = False

            print('\n')
            print('Turno del jugador: ', jugador['nombre'])
            print('Tablero: ', posicion)
            mostrarSubtablero(subtablero)
            sub = copy.deepcopy(subtablero)
            if jugador['marca'] == jugador1:
                estado1 = State(sub)
                root = MonteCarloTreeSearchNode(state=estado1, isMax=True)
                pos = root.best_action().parent_action
            else:
                estado1 = State(sub)
                root = MonteCarloTreeSearchNode(state=estado1, isMax=True)
                pos = root.best_action().parent_action

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
    imprimirTablero(tablero)
    print('El ganador es!!!: ', ganador)
    return ganador

def juegoMinMaxVSRandom():
    tablero = crearTablero()
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
                opcion = np.random.randint(1,10)
                subtablero, posicion = obtenerTablero(opcion, tablero)
                primerTurno = False

            print('\n')
            print('Turno del jugador: ', jugador['nombre'])
            print('Tablero: ', posicion)
            mostrarSubtablero(subtablero)
            sub = copy.deepcopy(subtablero)
            if jugador['marca'] == jugador1:
                if len(subtablero.getMoves()) == 9:
                    pos = subtablero.getMoves()[np.random.randint(1,9)]
                else:
                    pos = minMaxMejorJugada(subtablero, subtablero.getMoves())
            else:
                pos = subtablero.getMoves()[np.random.randint(1,len(subtablero.getMoves()))]

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
    imprimirTablero(tablero)
    print('El ganador es!!!: ', ganador)
    return ganador

def juegoMCTSvsRandom():
    tablero = crearTablero()
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
                opcion = np.random.randint(1,10)
                subtablero, posicion = obtenerTablero(opcion, tablero)
                primerTurno = False

            print('\n')
            print('Turno del jugador: ', jugador['nombre'])
            print('Tablero: ', posicion)
            mostrarSubtablero(subtablero)
            sub = copy.deepcopy(subtablero)
            if jugador['marca'] == jugador1:
                #TODO Traer la jugada usando MCTS
                estado1 = State(sub)
                root = MonteCarloTreeSearchNode(state=estado1, isMax=True)
                pos = root.best_action().parent_action
            else:
                pos = subtablero.getMoves()[np.random.randint(1,len(subtablero.getMoves()))]

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
    imprimirTablero(tablero)
    print('El ganador es!!!: ', ganador)
    return ganador

def juegoRandomVSRandom():
    tablero = crearTablero()
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
                opcion = np.random.randint(1,10)
                subtablero, posicion = obtenerTablero(opcion, tablero)
                primerTurno = False

            print('\n')
            print('Turno del jugador: ', jugador['nombre'])
            print('Tablero: ', posicion)
            mostrarSubtablero(subtablero)
            sub = copy.deepcopy(subtablero)
            if jugador['marca'] == jugador1:
                pos = subtablero.getMoves()[np.random.randint(1,len(subtablero.getMoves()))]
            else:
                pos = subtablero.getMoves()[np.random.randint(1,len(subtablero.getMoves()))]

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
    imprimirTablero(tablero)
    print('El ganador es!!!: ', ganador)
    return ganador

def juegoMCTSvsMinMax():
    tablero = crearTablero()
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
                opcion = np.random.randint(1,10)
                subtablero, posicion = obtenerTablero(opcion, tablero)
                primerTurno = False

            print('\n')
            print('Turno del jugador: ', jugador['nombre'])
            print('Tablero: ', posicion)
            mostrarSubtablero(subtablero)
            sub = copy.deepcopy(subtablero)
            if jugador['marca'] == jugador1:
                #TODO Traer la jugada usando MCTS
                estado1 = State(sub)
                root = MonteCarloTreeSearchNode(state=estado1, isMax=True)
                pos = root.best_action().parent_action
            else:
                if len(subtablero.getMoves()) == 9:
                    pos = subtablero.getMoves()[np.random.randint(1,9)]
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
    imprimirTablero(tablero)
    #print('El ganador es!!!: ', ganador)
    return ganador

def torneo():


    r1Partida1 = 'Montecarlo' if juegoMCTSvsMinMax() == 'Jugador1' else 'MinMax'
    r1Partida2 = 'Montecarlo' if juegoMCTSvsRandom() == 'Jugador1' else 'Random'
    r1Partida3 = 'MinMax' if juegoMinMaxVSRandom() == 'Jugador1' else 'Random' 
    #__________________________________________________________
    if r1Partida1 == 'Montecarlo' and r1Partida2 == 'Montecarlo':
        r2Partida1 = 'Montecarlo'
    elif r1Partida1 == 'Montecarlo' and r1Partida2 == 'Random':
        r2Partida1 = 'Montecarlo' if juegoMCTSvsRandom() == 'Jugador1' else 'Random'
    elif r1Partida1 == 'MinMax' and r1Partida2 == 'Montecarlo':
        r2Partida1 = 'Montecarlo' if juegoMCTSvsMinMax() == 'Jugador1' else 'MinMax'
    elif r1Partida1 == 'MinMax' and r1Partida2 == 'Random':
        r2Partida1 = 'MinMax' if juegoMinMaxVSRandom() == 'Jugador1' else 'Random'   
    #__________________________________________________________  
    if r1Partida3 == 'MinMax':
        r2Partida2 = 'MinMax'
    else:
        r2Partida2 = 'Random'
    #__________________________________________________________    
    if r2Partida1 == 'Montecarlo' and r2Partida2 == 'MinMax':
        r3Partida1 = 'Montecarlo' if juegoMCTSvsMinMax() == 'Jugador1' else 'MinMax'
    elif r2Partida1 == 'MinMax' and r2Partida2 == 'MinMax':
        r3Partida1 = 'MinMax'
    elif r2Partida1 == 'Montecarlo' and r2Partida2 == 'Random':
        r3Partida1 = 'Montecarlo' if juegoMCTSvsRandom() == 'Jugador1' else 'Random'
    elif r2Partida1 == 'Random' and r2Partida2 == 'MinMax':
        r3Partida1 = 'MinMax' if juegoMinMaxVSRandom() == 'Jugador1' else 'Random'
    elif r2Partida1 == 'Random' and r2Partida2 == 'Random':
        r3Partida1 = 'Random'
    elif r2Partida1 == 'MinMax' and r2Partida2 == 'Random':
        r3Partida1 = 'MinMax' if juegoMinMaxVSRandom() == 'Jugador1' else 'Random'

    print('Ganadores primera Ronda!')
    print('Partida 1:', r1Partida1)
    print('Partida 2:', r1Partida2)
    print('Partida 3:', r1Partida3)
    print('Ganadores Segunda Ronda!')
    print('Partida 5:', r2Partida1)
    print('Ganador Ronda Final!')
    print('Partida 6:', r3Partida1)
    #return r3Partida1

torneo()
#juegoMCTSvsMinMax()
#juegoMinMaxVSminMax()
#juegoMCTSvsMCTS()
#juegoMCTSvsRandom()
#juegoMinMaxVSRandom()
#juegoRandomVSRandom()
#mc = 0
#mm = 0
#r = 0 
#for i in range(1001):
#    v = torneo()
#    if v == "Montecarlo":
#        mc += 1
#    elif v == "MinMax":
#        mm += 1
#    else:
#        r += 1

#print('Media Montecarlo: ', mc/1000)
#print('Media MinMax', mm/1000)
#print('Media Random', r/1000)