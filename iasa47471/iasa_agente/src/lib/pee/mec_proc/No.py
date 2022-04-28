# Esta classe representa um nó (node).
# Um nó é uma etapa de procura no processo de procura.
# Chamamos raiz ao nó correspondente ao estado inicial.

class No:
    def __init__(self, estado):
        self.estado = estado

    def __init__(self, estado, operador, antecessor):
        self.estado = estado
        self.operador = operador
        self.antecessor = antecessor

    def __lt__(self, no):
        # Retorna um boolean
        return