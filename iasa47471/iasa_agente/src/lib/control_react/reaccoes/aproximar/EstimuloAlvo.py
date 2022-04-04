from ecr.IEstimulo import IEstimulo

class EstimuloAlvo(IEstimulo):
    def __init__(self, direccao, gama=0.9):
        self._direccao = direccao
        self._gama = gama

    def detectar(percepcao):
        return super().detectar()