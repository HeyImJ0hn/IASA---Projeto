# Esta classe representa um nó (node).
# Um nó é uma etapa de procura no processo de procura.
# Chamamos raiz ao nó correspondente ao estado inicial.

class No:
    def __init__(self, estado):
        self.estado = estado

    def __init__(self, estado, operador=None, antecessor=None):
        self.estado = estado
        self.operador = operador
        self.antecessor = antecessor
        self._custo = 0
        self.profunidade = 0

    @property
    def custo(self):
        return self._custo

    def __it__(self, no):
        return self._custo < no._custo
