from abc import ABC, abstractmethod
from pee.mec_proc.No import No
from pee.mec_proc.fronteira.FronteiraPrioridade import FronteiraPrioridade

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

    def resolver(self, problema, f):
        no = No(problema.estado_inicial)
        fronteira = FronteiraPrioridade(f)
        explorados = []

        while not fronteira.vazia():
            no = fronteira.remover()
            if problema.objectivo(no.estado): return no
            for child in self.expandir(problema, no):
                s = child.estado
                if s not in explorados or child.custo < explorados[s].custo:
                    explorados[s] = child
                    fronteira.inserir(child)
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