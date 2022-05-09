from pee.aval.Avaliador import Avaliador

# Esta classe representa uma avaliação com base na função
# heurística - h(n)
# Nesta classe, que vai especificar a classe Avaliador, vamos
# apenas guardar a instancia da interface Heuristica entregue
# como argumento ao construtor.


class AvalHeur(Avaliador):
    def __init__(self, heuristica):
        self.heuristica = heuristica
