from ecr.Reaccao import Reaccao

class EvitarDir(Reaccao):
    def __init__(self, direccao, resposta):
        super().__init__()
        self._direccao = direccao
        self._resposta = resposta