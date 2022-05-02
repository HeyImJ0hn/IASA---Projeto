from abc import ABC, abstractmethod

# Esta classe representa uma fronteira de exploração.
# A fronteira de exploração é uma estrutura de dados com
# relaçãode ordem e faz parte do mecanismo de procura.
# O critério de ordenação determina a estratégia de controlo da procura.

class Fronteira(ABC):
    def __init__(self):
        self.nos = [9]

    # Verifica se a lista de nos está vazia
    def vazia(self):
        if not self.nos:
            return True
        return False

    @abstractmethod
    def inserir(no):
        pass

    # Remove o primeiro nó da lista de nós
    def remover(self):
        return self.nos.pop(0)