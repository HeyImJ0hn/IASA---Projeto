from resposta.RespostaMover import RespostaMover
from sae.ambiente.direccao import Direccao


class RespostaEvitar(RespostaMover):
    def __init__(self, dir_inicial=Direccao.ESTE):
        super().__init__(dir_inicial)

    def activar(self, percepcao, intensidade=0):
        if (percepcao.contacto_obst(self.dir_inicial)):
            direccao = self.direccao_livre(percepcao)
            if (direccao):
                percepcao.direccao = direccao
                accao = super().activar(percepcao, intensidade)
            else:
                return
        else:
            accao = super().activar(percepcao, intensidade)
        return accao

    def direccao_livre(percepcao):
        # Retorna Direccao
        return
