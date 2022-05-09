from abc import ABC, abstractmethod
from pee.aval.Avaliador import Avaliador
from pee.larg.ProcuraGrafo import ProcuraGrafo
from pee.mec_proc.fronteira.FronteiraPrioridade import FronteiraPrioridade

# Esta classe representa um mecanismo de procura melhor-primeiro (best-first).
# Esta procura tira partido de uma avaliação do estado e utiliza a função f
# para avaliação de cada nó gerado.
# f(n) >= 0; Geralmente f(n) representa uma estimativa do custo da solução
# através do nó n. Quanto menor o valor de f(n) mais promissor é o nó n.
# Nesta procura a fronteira de expliração é ordenada por ordem crescente de f(n)


class ProcuraMelhorPrim(ProcuraGrafo):
    def _iniciar_fronteira():
        return FronteiraPrioridade(Avaliador())

    def _manter(no):
        return super()._manter()

    @abstractmethod
    def iniciar_avaliador():
        pass
