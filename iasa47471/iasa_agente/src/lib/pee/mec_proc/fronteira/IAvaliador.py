from abc import ABC, abstractmethod

# Interface

class IAvaliador(ABC):

    @abstractmethod
    def prioridade(self, no):
        pass