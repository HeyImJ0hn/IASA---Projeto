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
    # Retorna uma accao 
    #
    # É criada uma lista de accoes vazia no inicio do método.
    # De seguida é percorrida a lista de comportamentos
    # entregue na criação da instancia da classe e é guardada a ação
    # retornada pelo método "activar" de cada comportamento.
    # Caso a accao exista, é adicionada à lista de accoes criada
    # inicialmente. No fim é corrido o método "seleccionar_accao" e retorna
    # a accao selecionada conforme o método de seleccao usado.
    def activar(self, percepcao):
        accoes = []
        for comp in self._comportamentos:
            accao = comp.activar(percepcao)
            if accao:
                accoes.append(accao)
        return self.seleccionar_accao(accoes)

    # Método abstrato
    # Seleciona uma accao da lista de accoes entregue
    # através dos métodos de seleção "Hierarquia",
    # "Prioridade" ou "Fusão" (não implementado)
    # e retorna a accao selecionada
    @abstractmethod
    def seleccionar_accao(accoes):
        '''
        Selecionar accao
        @param percepcao: lista de accoes
        @return: acção selecionada
        '''
        pass