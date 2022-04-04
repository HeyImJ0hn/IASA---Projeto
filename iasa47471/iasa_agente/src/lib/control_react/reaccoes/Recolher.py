from ecr.Hierarquia import Hierarquia

# Classe Recolher - Extende a classe Hierarquia.
# Representa um dos objetivos do agente.
# A classe recolher vai usar a Hierarquia como
# método de selecção de acção.

class Recolher(Hierarquia):
    # Recebe uma lista de comportamentos que vao mais tarde
    # ser selecionados de acordo com um método de selecção
    def __init__(self, comportamentos):
        super().__init__(comportamentos)

    # Vai usar o método de seleccção "Hierarquia" para
    # selecionar, das várias accoes, a acção a executar
    def seleccionar_accao(accoes):
        return super().seleccionar_accao()
