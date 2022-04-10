from ecr.IEstimulo import IEstimulo

# Classe EstimuloObst - Implementa IEstimulo
# Esta classe representa o estímulo detetado
# pelo agente quando este é um obstáculo.
# Vai permitir ao agente reagir quando encontrar
# um obstaculo.


class EstimuloObst(IEstimulo):
    # O construtor recebe como argumentos uma direccao e um
    # valor de intensidade. A intensidade é um float e caso não seja
    # entregue ao construtor este valor é 1.0.
    def __init__(self, direccao, intensidade=1.0):
        self._direccao = direccao
        self._intensidade = intensidade

    # Detecta o estímulo através da percepcao
    # entregue como argumento e verifica
    # se há algum contacto com um obstáculo.
    # Se sim retorna a intensidade inicial. Se não retorna 0.
    def detectar(self, percepcao):
        if (percepcao.contacto_obst(self._direccao)):
            return self._intensidade
        return 0
