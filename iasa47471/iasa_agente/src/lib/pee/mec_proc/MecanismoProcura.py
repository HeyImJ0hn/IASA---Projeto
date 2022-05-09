from abc import ABC, abstractmethod
from pee.Solucao import Solucao
from pee.mec_proc.No import No
# Esta classe representa um mecanismo geral de procura.
# Existem vários mecanismos de procura como a procura em profundidade,
# a procura em largura, procura em grafos e a procura melhor-primeiro.
# Um processo de procura é uma exploração sucessiva do espaço de estados e
# a sua etapa de procura é um nó.
# O processo de procura é composto por uma árvore de procura, com uma raiz
# que é o nó correspondente ao estado inicial, e uma fronteira de exploração, ou
# estrutura de dados com relação de ordem, em que o critériode ordenação determina
# a estratégia de controlo da procura.


class MecanismoProcura(ABC):
    def __init__(self):
        self.fronteira = self._iniciar_fronteira()

    def resolver(self, problema):
        no = No(problema.estado_inicial)
        self._memorizar(no)

        while not self.fronteira.vazia():
            no_explorado = self.fronteira.remover()
            print(no_explorado)
            if problema.objectivo(no_explorado.estado):
                return Solucao(no_explorado)
            for child in self.expandir(problema, no):
                self._memorizar(child)
        return "failure"

    @abstractmethod
    def _iniciar_fronteira():
        pass

    def expandir(self, problema, no):
        for operador in problema.operadores:
            estado_suc = operador.aplicar(no.estado)
            if (estado_suc):
                yield No(estado_suc, operador, no)

    @abstractmethod
    def _memorizar(no):
        pass
