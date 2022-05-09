from abc import ABC, abstractmethod

# Este método abstrato vai ser usado como base
# para a clase AvalHeur, que por sua vez vai ser usada
# nos avaliadores de Sofrega e AA (A*).


class Avaliador(ABC):

    @abstractmethod
    def prioridade(self, no):
        pass
