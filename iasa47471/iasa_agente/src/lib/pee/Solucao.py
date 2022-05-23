# Esta classe representa uma solução do método de procura.

from mod.Estado import Estado
from pee.PassoSolucao import PassoSolucao


class Solucao:
    def __init__(self, no_final):
        self.percurso = []
        no = no_final
        while no:
            self.percurso.insert(0, no)
            no = no.antecessor

    # Remover o primeiro passo do percurso
    def remover_passo(self):
        estado = self.percurso[-1].operador
        operador = self.percurso.pop(0)
        return PassoSolucao(estado, operador)

    def __iter__(self):
        return iter(self.percurso)

    def __getitem__(self, index):
        return self.percurso[index]
