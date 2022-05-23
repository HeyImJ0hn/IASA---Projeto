from abc import ABC, abstractmethod

# Interface ModeloPlan
# Representa um modelo de planeamento usado no planeador,
# como por exemplo o Modelo Mundo.

class ModeloPlan(ABC):
    @abstractmethod
    def estado(self):
        return

    @abstractmethod
    def estados(self):
        return

    @abstractmethod
    def operadores(self):
        return
