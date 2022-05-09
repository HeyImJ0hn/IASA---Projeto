from abc import ABC, abstractmethod

# Esta interface tem como objetivo representar a função heurística - h(n).
# Esta função representa uma estimativa do custo do percurso desde
# o nó "n" até ao nó objetivo.
# Reflete conhecimento acerta do domínio do problema para guiar a procura.
# É também importante referir que o seu valor é independente do
# percurso até "n" e depende apenas do estado associado a "n"
# e do objetivo.
# A funcção heuristica vai ser usada no cálculo do custo
# da procura A* e procura sôfrega.


class Heuristica(ABC):

    @abstractmethod
    def h(estado):
        # Retorna double
        pass
