from pee.Fronteira import Fronteira
from heapq import heappush, heappop

# Representa um tipo de fronteira, Fronteira Prioridade.

class FronteiraPrioridade(Fronteira):
    def __init__(self, avaliador):
        self.avaliador = avaliador

    def inserir(self, no):
        prioridade = self.avaliador.prioridade(no)
        heappush(self.nos, (prioridade, no))
        return

    def remover(self):
        _, no = heappop(self.nos)
        return no