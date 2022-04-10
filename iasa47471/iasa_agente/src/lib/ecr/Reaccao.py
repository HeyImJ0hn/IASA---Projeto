from ecr.IComportamento import IComportamento

# Esta classe representa uma reação
# Cada reação é composta por um estímulo, que causa a reação,
# e por uma resposta a esse estímulo
# Numa arquitetura reativa simples as ações são ativadas diretamente
# em função das percepções, e não são mantidas representações internas
# do estado do mundo.


class Reaccao(IComportamento):
    def __init__(self, estimulo, resposta):
        self._estimulo = estimulo
        self._resposta = resposta

    # Este método vai ser chamado quando for então detetado um estímulo por outra
    # classe.
    # É entregue a percepcao e através do método "detectar" da classe "Estimulo" é
    # possível obter a intensidade do estímulo.
    # Case a intensidade seja maior que 0 é ativada uma resposta e retornada a ação
    # para que esta seja executada.
    # Retorna uma variável do tipo Accao
    def activar(self, percepcao):
        intensidade = self._estimulo.detectar(percepcao)
        if (intensidade > 0):
            return self._resposta.activar(percepcao, intensidade)
        return None
