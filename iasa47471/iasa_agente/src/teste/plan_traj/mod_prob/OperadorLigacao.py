# Esta classe representa uma estrutura de dados, OperadorLigacao
# Representa também uma ação
# Gera uma transformação de estado através do método aplicar.

from teste.plan_traj.mod_prob.EstadoLocalidade import EstadoLocalidade


class OperadorLigacao:
    def __init__(self, origem, destino, custo):
        self.origem = EstadoLocalidade(origem)
        self.destino = EstadoLocalidade(destino)
        self._custo = custo

    def aplicar(self, estado):
        if self.origem == estado:
            return self.destino

    def custo(self, estado, estado_suc):
        return self.custo