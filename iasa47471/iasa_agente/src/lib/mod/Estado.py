from abc import ABC, abstractmethod

# Esta classe representa um estado.
# Um estado representa uma situação ou configuração na resolução
# de um problema. Tem também uma identificação única (id).

class Estado(ABC):
    
    @abstractmethod
    def id_valor():
        pass

    def __hash__(self):
        return self.id_valor

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()