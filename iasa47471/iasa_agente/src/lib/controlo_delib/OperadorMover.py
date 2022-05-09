import math
from mod.IOperador import IOperador
from mod.agente.EstadoAgente import EstadoAgente
from sae.agente.accao import Accao

# Esta classe representa um tipo de operador, OperadorMover, que permite
# ao agente mover-se no ambiente, tendo em conta o custo de cada translação.
# Recebe no seu construtor um modelo mundo e um angulo, que vão ser guardados. É
# também criada, dentro do construtor, uma ação (Accao) onde é entregue o angulo.
# As variaveis modelo_mundo e ang são variáveis do tipo Read Only.

class OperadorMover(IOperador):
    def __init__(self, modelo_mundo, ang):
        self._modelo_mundo = modelo_mundo
        self._ang = ang
        self._accao = Accao(ang)

    @property
    def ang(self):
        return self.ang

    @property
    def accao(self):
        return self._accao

    # Movimenta o agente de acordo com uma translação matemática.
    # É feita uma verificação para saber se o novo estado é
    # válido ou não.
    # Retorna um estado se este for válido.
    def aplicar(self, estado):
        x, y = estado.posicao
        dx = round(self._accao.passo * math.cos(self._ang))
        dy = round(self._accao.passo * math.sin(self._ang))
        nova_posicao = x + dx, y + dy
        novo_estado = EstadoAgente(nova_posicao)
        if novo_estado in self._modelo_mundo.estados():
            return novo_estado

    # Retorna o custo da translação.
    # É calculada a distancia entre a posicao do estado atual e do próximo estado
    # e esta depois é usada para verificar o máximo entre a distancia e 1, ou o custo. 
    def custo(self, estado, novo_estado):
        return max(math.dist(estado.posicao, novo_estado.posicao), 1)
