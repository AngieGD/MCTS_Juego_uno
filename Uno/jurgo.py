class Estado:
    def __init__(self , cartas_jugadas , numero_cartas_jugador , numero_cartas_ia , carta_actual , cartas_mazo_ia):
        self.cartas_jugadas = cartas_jugadas #cartas que ya no se pueden usar
        self.numero_cartas_jugador = numero_cartas_jugador
        self.numero_cartas_ia = numero_cartas_ia
        self.carta_actual = carta_actual #de esta carta depende el siguiente movimiento
        self.cartas_mazo_ia = cartas_mazo_ia
        self.hijos = []



    def esFinal(self): #Para finalizar el juego
        return True if (self.numero_cartas_jugador == 0 or self.numero_cartas_ia == 0) else False #Algun jugador queda sin cartas

    def posibles_jugadas(self):
        return list()

    def seleccionar_jugada(self):
        jugadas_candidatas = []
        for carta in self.cartas_mazo_ia: #idea: crear metodo que retorne las posibles jugadas
            if carta in self.posibles_jugadas():
                jugadas_candidatas.append(carta)

        return jugadas_candidatas

    




        

    def generarHijos(self):
        pass


   

    



