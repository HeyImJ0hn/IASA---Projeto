# Esta classe representa a resposta a um estímulo.
# É usada na classe "Reaccao" quando é necessário obter a resposta a um
# estímulo.
# Uma resposta é uma ação diretamente ativada em função das percepções.
# As respostas a alterações no ambiente são rápidas,
# e aos estímulos do ambiente são fixas e predefinidas

class Resposta:
    def __init__(self, accao):
        self._accao = accao

    # Quando é ativado, dependendo da intensidade, é retornada a ação referente à
    # percepcao.
    # Retorna uma variável do tipo Accao
    def activar(self, percepcao, intensidade):
        self._accao.prioridade = intensidade
        return self._accao