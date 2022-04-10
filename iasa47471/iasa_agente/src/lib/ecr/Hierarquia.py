import re
from ecr.ComportComp import ComportComp

# Classe extende a classe ComportComp.
# Esta classe representa uma das formas de seleccao
# de accoes, a seleccao por Hierarquia.
# A accao é selecionada através da hierarquia, portanto,
# a accao selecionada é a primeira de uma lista de accoes


class Hierarquia(ComportComp):

    # Recebe uma lista de accoes e seleciona uma
    # de acordo com o método de seleção "Hierarquia"
    # A primeira accao tem prioridade, ou seja,
    # as accoes sao selecionadas pela sua ordem na lista.
    # Retorna a accao selecionada.
    def seleccionar_accao(self, accoes):
        if accoes:
            return accoes[0]
