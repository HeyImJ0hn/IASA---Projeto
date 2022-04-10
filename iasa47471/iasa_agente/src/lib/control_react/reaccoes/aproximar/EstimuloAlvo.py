from ecr.IEstimulo import IEstimulo
from sae.ambiente.elemento import Elemento

# Classe EstimuloAlvo - Implementa IEstimulo
# Esta classe representa o estímulo detetado
# pelo agente quando este é um alvo.
# Vai permitir ao agente reagir quando encontrar um alvo.


class EstimuloAlvo(IEstimulo):
    # Construtor vai receber uma direccao e a gama.
    # Caso o construtor nao receba um valor de gama,
    # o valor default é 0.9
    def __init__(self, direccao, gama=0.9):
        self._direccao = direccao
        self._gama = gama

    # Este método vai, a partir da percepcao,
    # retornar a intensidade caso o elemento
    # seja um alvo.
    # É possível, através da percepcao, retirar duas
    # variáveis, um elemento e a distancia.
    # É feita uma verificação para saber se o elemento encontrado
    # é um alvo ou não e se for é feito o calculo da intensidade
    # com a distancia obtida anteriormente e a game entregue ao
    # construtor.
    def detectar(self, percepcao):
        elemento, distancia, _ = percepcao[self._direccao]
        if elemento == Elemento.ALVO:
            # Calculo da intensidade
            return self._gama ** distancia
        return 0
