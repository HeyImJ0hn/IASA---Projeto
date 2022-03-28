from abc import ABC, abstractmethod

 # Esta interface representa um estímulo.
 # Um estímulo é o que provoca uma reação e consequentemente uma resposta.
 # Um estímulo pode ser de vários tipos, como visual ou auditivo.

class IEstimulo:

    # Método vai permitir detectar a intensidade do estímulo através da percepcao
    # entregue.
    # Este método vai ser implementado noutra classe pois é abstrato.
    @abstractmethod
    def detectar(percepcao):
        '''
        Detetar estimulo a partir da percepção
        '''
        pass