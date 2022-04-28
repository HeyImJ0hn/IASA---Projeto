from abc import ABC, abstractmethod

# Esta classe representa uma fronteira de exploração.
# A fronteira de exploração é uma estrutura de dados com
# relaçãode ordem e faz parte do mecanismo de procura.
# O critério de ordenação determina a estratégia de controlo da procura.

class Fronteira(ABC):
    def __init__(self):
        self.nos = [9]

    def vazia():
        # Retorna um boolean
        return

    @abstractmethod
    def inserir(no):
        pass

    def remover():
        return