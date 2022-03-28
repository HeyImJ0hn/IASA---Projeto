from ecr.ComportComp import ComportComp

# Classe extende a classe ComportComp.
# Esta classe representa uma das formas de seleccao
# de accoes, a seleccao por Prioridade.
# A accao selecionada é a accao com maior prioridade.
# Cada objeto do tipo "Accao" tem um atributo prioridade.
class Prioridade(ComportComp):

    # Recebe uma lista de accoes e seleciona uma
    # de acordo com o método de seleção "Prioridade".
    # Verifica a lista de accoes e retorna a accao com 
    # maior prioridade
    # Retorna a accao selecionada
    def seleccionar_accao(self, accoes):
        if accoes:
            return max(accoes, key=lambda accao: accao.prioridade)