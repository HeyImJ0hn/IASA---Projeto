from control_react.reaccoes.aproximar.AproximarDir import AproximarDir
from ecr.Prioridade import Prioridade
from sae.ambiente.direccao import Direccao

# Classe AproximarAlvo - Extende a classe Prioridade.
# É um comportamento composto e representa uma reaccao
# do agente no ambiente.
# Este comportamento, assim como os comportamentos EvitarObst
# e explorar, fazem parte de um comportamento maior, Recolher.
#
# Vai permitir ao agente aproximar-se do alvo.


class AproximarAlvo(Prioridade):
    # Neste construtor é criada uma lista com 4 comportamentos
    # "AproximarDir". Cada um deste comportamentos recebe como argumento
    # uma direção diferente do enum "Direccao".
    # A lista é depois entregue ao construtor da superclasse.
    def __init__(self):
        super().__init__([AproximarDir(direccao) for direccao in Direccao])
