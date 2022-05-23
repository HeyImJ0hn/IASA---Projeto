from abc import ABC, abstractmethod

# Interface Planeador
# Um planeador tem um raciocínio automático orientado para a geração de 
# estratégias ou planos de ação, em particular para execução por agentes inteligentes.
# Tem também diferentes métodos de planeamento automático, tendo por base mecanismos
# de procura em espaços de estados e processos de decisão de Markov.

class Planeador(ABC):
    @abstractmethod
    def __init__(self):
        return

    # Com uma lista de objetivos e um modelo de planeamento,
    # neste caso modelo mundo, é gerado um novo plano.    
    @abstractmethod
    def planear(self, modelo_mundo, objetivos):
        return

    # Termina o plano gerado anteriormente.
    @abstractmethod
    def terminar_plano(self):
        pass

    @abstractmethod
    def obter_accao(self, estado):
        return