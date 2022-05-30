from abc import ABC, abstractmethod

# Esta interface representa um modelo do mundo, 
# neste caso Modelo PDM (Processos de Decisão de Markov).
# A propriedade de Markov diz que os estados futuros dependem 
# apenas do estado atual, ou seja, são independentes de estados passados.

class ModeloPDM(ABC):
    
    # Representa um conjunto de estados do mundo
    @abstractmethod
    def S(self):
        pass

    # Representa um conjunto de açoes para um determinado estado
    @abstractmethod
    def A(self, s): 
        pass

    # Representa uma transição de "s" para "s'"
    @abstractmethod
    def T(self, s, a):
        pass

    # Representa a recompensa dos estados
    @abstractmethod
    def R(self, s, a, sn):
        pass
