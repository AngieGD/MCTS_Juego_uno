jugador1, jugador2 = 'O', 'X'
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