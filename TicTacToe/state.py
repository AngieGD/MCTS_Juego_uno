

class State:

    def __init__(self, state):
        self.state = state
        self.j1 = 'O'
        self.j2 = 'X'

    def get_legal_actions(self):
        return self.state.getMoves()

    def is_game_over(self):
        return (self.state.victoriaJugador(self.j1) or self.state.victoriaJugador(self.j2) or len(self.state.getMoves()) < 1)

    def game_result(self):
        if self.state.victoriaJugador(self.j1):
            #print('Bandera 1')
            return 1
        if self.state.victoriaJugador(self.j2):
            #print('Bandera -1')
            return -1
        #print('Bandera 0')    
        return 0

    def move(self, action, isMax):
        if isMax:
            self.state.insertarMarca(action, 'O')
        else:
            self.state.insertarMarca(action, 'X')
        return self
    
    def imprimir(self):
        for i in range(3):
            print(self.state.table[i])