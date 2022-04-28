from abc import ABC, abstractmethod

# Esta classe representa a interface Operador.
# Um operador representa uma ação ou uma transformação de estado.

class IOperador(ABC):
    
    @abstractmethod
    def aplicar(estado):
        pass

    @abstractmethod
    def custo(estado, estado_suc):
        pass
