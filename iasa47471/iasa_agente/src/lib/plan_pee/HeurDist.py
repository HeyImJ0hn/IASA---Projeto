from pee.aval.Heuristica import Heuristica

class HeurDist(Heuristica):
    def __init__(self, estado):
        self.estado = estado

    def h(self, estado):
        return super().h()