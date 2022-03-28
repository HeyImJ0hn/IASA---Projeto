from ecr.Resposta import Resposta

# Classe extende a classe Resposta
# Permite mover o agente na direção pretendida
# consoante a resposta
class RespostaMover(Resposta):
    # Construtor da classe
    # Recebe uma direção
    def __init__(self, direccao):
        self._direccao = direccao