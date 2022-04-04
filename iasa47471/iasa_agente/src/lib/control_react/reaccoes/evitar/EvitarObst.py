from ecr.Hierarquia import Hierarquia

# Classe EvitarObst - Extende a classe Hierarquia.
# Representa um dos objetivos do agente.
# A classe EvitarObst vai usar a Hierarquia como
# método de selecção de acção.
# Permite ao agente evitar os obstaculos do ambiente.

class EvitarObst(Hierarquia):
    def __init__(self):
        return