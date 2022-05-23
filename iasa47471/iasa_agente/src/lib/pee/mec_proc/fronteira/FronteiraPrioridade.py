from heapq import heappush, heappop

from pee.mec_proc.fronteira.Fronteira import Fronteira

# Representa um tipo de fronteira, Fronteira Prioridade.

class FronteiraPrioridade(Fronteira):
    def __init__(self, avaliador):
        super().__init__()
        self.avaliador = avaliador

    def inserir(self, no):
        prioridade = self.avaliador.prioridade(no)
        heappush(self.nos, (prioridade, no))

    def remover(self):
        _, no = heappop(self.nos)
        return no