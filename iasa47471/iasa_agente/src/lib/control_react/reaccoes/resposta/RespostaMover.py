from sae import Accao
from ecr.Resposta import Resposta

# Classe extende a classe Resposta
# Esta classe permite mover o agente numa determinada direçao
# através da sua superclasse "Resposta" e de accoes
class RespostaMover(Resposta):

    # Construtor da classe
    # Recebe uma direção.
    # É usado o construtor da superclasse "Resposta" e
    # é entregue a esse construtor uma instância nova de Accao
    # com a direção entregue inicialmente a este construtor.
    def __init__(self, direccao):
        super().__init__(Accao(direccao))