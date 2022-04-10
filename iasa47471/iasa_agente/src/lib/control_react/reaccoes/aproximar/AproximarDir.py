from control_react.reaccoes.aproximar.EstimuloAlvo import EstimuloAlvo
from control_react.reaccoes.resposta.RespostaMover import RespostaMover
from ecr.Reaccao import Reaccao

# Classe AproximarDir - Extende a classe Reaccao.
# Esta classe representa uma reaccao a um estímulo
# do agente no ambiente.
# Vai permitir ao agente aproximar-se de uma direcção.
# A classe AproximarAlvo vai instanciar várias vezes esta classe,
# de modo a obter uma instancia para cada direccao.


class AproximarDir(Reaccao):
    # Neste construtor são criadas duas instâncias,
    # uma da classe "EstimuloAlvo" e outra da classe "RespostaMover".
    # Ambas as instâncias recebem uma direccao. Direccao que foi entregue
    # no construtor desta classe (AproximarDir).
    # Estas duas instancias são então entregues ao construtor da superclasse.
    def __init__(self, direccao):
        super().__init__(EstimuloAlvo(direccao), RespostaMover(direccao))
