# Esta classe representa um nó (node).
# Um nó é uma etapa de procura no processo de procura.
# Chamamos raiz ao nó correspondente ao estado inicial.

class No:
    def __init__(self, estado, operador=None, antecessor=None):
        self._estado = estado
        self._operador = operador
        self._antecessor = antecessor
        self._custo = 0
        self._profunidade = 0

    @property
    def custo(self):
        return self._custo

    @property
    def estado(self):
        return self._estado

    @property
    def operador(self):
        return self._operador
    
    @property
    def antecessor(self):
        return self._antecessor

    @property
    def profundidade(self):
        return self._profunidade

    def __it__(self, no):
        return self._custo < no.custo()
