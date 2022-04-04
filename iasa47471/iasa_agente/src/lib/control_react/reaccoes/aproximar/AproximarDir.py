from ecr.Reaccao import Reaccao

# Classe AproximarDir - Extende a classe Reaccao.
# Esta classe representa uma reaccao a um estímulo
# do agente no ambiente.
# Vai permitir ao agente aproximar-se de uma direcção.
# A classe AproximarAlvo vai usar várias vezes esta
# classe de modo a aproximar-se do alvo.

class AproximarDir(Reaccao):
    def __init__(self, direccao):
        self._direccao = direccao