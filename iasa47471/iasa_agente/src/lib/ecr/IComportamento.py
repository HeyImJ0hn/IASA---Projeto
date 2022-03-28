from abc import ABC, abstractmethod

# Esta interface representa um comportamento.
# Um comportamento é qualquer tipo de reação, relacionando padrões de percepção
# com padrões de ação. Pode também ter continuidade no tempo.

class IComportamento:

    # Este método vai permitir, através de uma percepcao, executar uma accao.
    # Sendo este método abstrato, vai ser implementado noutra
    # classe.
    @abstractmethod
    def activar(percepcao):
        pass