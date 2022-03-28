from abc import ABC, abstractmethod
import IComportamento

# Esta classe representa um comportamento composto.
# Um comportamento pode ser composto por outros comportamentos,
# criado assim um comportamento composto.
# Esta classe implementa a interface IComportamento
class ComportComp(IComportamento):
    # Construtor da classe ComportComp
    # Recebe uma lista de comportamentos
    def __init__(self, comportamentos):
        self._comportamentos = comportamentos

    # Ativa uma accao a partir da percepcao recebida
    # Retorna a accao ativada
    def activar(percepcao):
        # TODO
        return None

    # Método abstrato
    # Seleciona uma accao da lista de accoes entregue
    @abstractmethod
    def seleccionar_accao(accoes):
        '''
        Selecionar accao
        @param percepcao: lista de accoes
        @return: acção selecionada
        '''