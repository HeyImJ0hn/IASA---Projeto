from ecr.IEstimulo import IEstimulo

class EstimuloObst(IEstimulo):
    def __init__(self, direccao, intensidade=1):
        self._direccao = direccao
        self._intensidade = intensidade