# Esta classe representa a resposta a um estímulo.
# É usada na classe "Reaccao" quando é necessário obter a resposta a um
# estímulo.
# Uma resposta é uma ação diretamente ativada em função das percepções.
# As respostas a alterações no ambiente são rápidas,
# e aos estímulos do ambiente são fixas e predefinidas.
class Resposta:
    def __init__(self, accao):
        self.accao = accao

    # Quando é ativado, é atualizada a prioridade da accao entregue
    # no construtor da classe para o valor da intensidade entregue como
    # parametro no método.
    # Caso nao seja entregue nenhum valor de intensidade, o valor
    # default é 0.
    # Retorna a accao com a nova prioridade.
    def activar(self, percepcao, intensidade=0):
        self.accao.prioridade = intensidade
        return self.accao
