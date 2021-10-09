import numpy as np
from collections import defaultdict
import copy
class MonteCarloTreeSearchNode:

    def __init__(self, state, isMax, parent=None, parent_action=None):
        #print(isMax)
        self.state = state#Representa el estado del tablero
        self.parent = parent#es none para el nodo raíz y para otros nodos es igual al nodo del que se deriva
        self.parent_action = parent_action#Es igual a la acción que realizo el padre, si es la raiz, es none
        self.children = []#Contiene las posibles jugadas del estado actual
        self._number_of_visits = 0#número de veces que se visita el nodo actual
        self._results = defaultdict(int)#Diccionario
        self._results[1] = 0    
        self._results[-1] = 0
        #self._untried_actions = None
        self._untried_actions = self.untried_actions()#Representa la lista de todas las acciones posibles
        self.isMax = isMax
        #return

    #Regresa una lista con las jugada a partir del estado actual
    def untried_actions(self):
        #print('Prueba: ',self.state.get_legal_actions())
        self._untried_actions = self.state.get_legal_actions()
        return self._untried_actions
    
    #Regresa la diferencia de victorias - derrotas
    def q(self):
        wins = self._results[1]
        loses = self._results[-1]
        return wins - loses
    
    #Regresa el número de veces que se vista cada estado
    def n(self):
        return self._number_of_visits

    #A partir del estado actual, se genera el siguiente estado en función de la acción que se lleve a cabo. 
    # En este paso, todos los posibles nodos secundarios correspondientes a los estados generados se añaden 
    # a la matriz secundaria y se devuelve child_node. Todos los estados que son posibles a partir del estado 
    # actual se generan y se devuelve el child_node correspondiente a este estado generado.
    def expand(self):
        action = self._untried_actions.pop()
        next_state = self.state.move(action, self.isMax)#Generar un nuevo estado - Arreglar luego
        #print('bandera', next_state.get_legal_actions())
        child_node = MonteCarloTreeSearchNode(
            next_state, not self.isMax, parent=self, parent_action=action)
        self.children.append(child_node)
        return child_node 
    
    #Esto se usa para verificar si el nodo actual es terminal o no. Se llega al nodo terminal cuando termina 
    # el juego.
    def is_terminal_node(self):
        return self.state.is_game_over()
    
    #Desde el estado actual, se simula todo el juego hasta que hay un resultado para el juego. Este resultado 
    #del juego se devuelve. Por ejemplo, si resulta en una victoria, el resultado es 1. De lo contrario, es -1 
    #si resulta en una pérdida. Y es 0 si es un empate. Si todo el juego se simula aleatoriamente, es decir, 
    #en cada turno el movimiento se selecciona aleatoriamente de un conjunto de movimientos posibles, se llama 
    #playout ligero.
    def rollout(self):
        current_rollout_state = self.state
        #print('Prueba rollout')
        turn = self.isMax
        while not current_rollout_state.is_game_over():
            possible_moves = current_rollout_state.get_legal_actions()
            action = self.rollout_policy(possible_moves)
            current_rollout_state = current_rollout_state.move(action, turn)
            turn = not turn
        return current_rollout_state.game_result()
    
    #En este paso se actualizan todas las estadísticas de los nodos. Hasta que se alcanza el nodo principal, 
    # el número de visitas para cada nodo se incrementa en 1. Si el resultado es 1, es decir, resultó en una 
    # ganancia, entonces la ganancia se incrementa en 1. De lo contrario, si el resultado es una pérdida, 
    # entonces la pérdida se incrementa en 1.
    def backpropagate(self, result):
        self._number_of_visits += 1.
        self._results[result] += 1.
        if self.parent:
            self.parent.backpropagate(result)
    
    #Todas las acciones salen de _untried_actions una por una. Cuando se vacía, es decir, cuando el tamaño
    #  es cero, se expande por completo.
    def is_fully_expanded(self):
        return len(self._untried_actions) == 0
    
    #Una vez completamente expandida, esta función selecciona el mejor niño de la matriz de niños. El primer
    #  término de la fórmula corresponde a la explotación y el segundo término corresponde a la exploración.
    def best_child(self, c_param=0.1):
        choices_weights = [(c.q() / c.n()) + c_param * np.sqrt((2 * np.log(self.n()) / c.n())) for c in self.children]
        return self.children[np.argmax(choices_weights)]
    
    #Selecciona aleatoriamente un movimiento entre los posibles movimientos. Este es un ejemplo de reproducción 
    # aleatoria.
    def rollout_policy(self, possible_moves):
        return possible_moves[np.random.randint(len(possible_moves))]
    
    #Selecciona el nodo para ejecutar el despliegue.
    def _tree_policy(self):
        #Creamos una copia del nodo actual
        current_node = self
        #Evaluamso que el nodo no sea terminal, si no es terminal iteramos
        while not current_node.is_terminal_node():
            #Si el nodo actual no se ha expandido lo hacemos
            if not current_node.is_fully_expanded():
                return current_node.expand()
            else:
                current_node = current_node.best_child()
        return current_node

    #Esta es la mejor función de acción que devuelve el nodo correspondiente al mejor movimiento posible. 
    # El paso de expansión, simulación y retropropagación se lleva a cabo mediante el código Siguiente.
    def best_action(self):
        simulation_no = 100
        for i in range(simulation_no):
            
            v = self._tree_policy()
            reward = v.rollout()
            v.backpropagate(reward)
        
        return self.best_child(c_param=0.)
    
