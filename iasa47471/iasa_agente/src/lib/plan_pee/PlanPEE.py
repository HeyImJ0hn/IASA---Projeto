from multiprocessing.spawn import import_main_path
from pee.inf.ProcuraInformada import ProcuraInformada
from pee.melhor_prim.ProcuraCustoUnif import ProcuraCustoUnif
from plan.Planeador import Planeador
from plan_pee.HeurDist import HeurDist
from plan_pee.ProblemaPlan import ProblemaPlan

# Esta classe representa um tipo de planeador, Planeador Procura em Espaços de Estados.
# Implementa a interface Planeador.
#
# Vai criar e gerir um plano de acordo com a procura em espaços de estados.
class PlanPEE(Planeador):
    def __init__(self):
        self._mec_pee = ProcuraInformada()

    # Gera um plano internamente
    def planear(self, modelo_plan, objetivos):
        estado_final = objetivos[0]
        heuristica = HeurDist()
        problema = ProblemaPlan(modelo_plan, estado_final)
        self._solucao = self._mec_pee.resolver(problema, heuristica)

    def obter_accao(self, estado):
        return super().obter_accao(estado)

    def terminar_plano(self):
        return super().terminar_plano()

    def plano_valido(self, estado):
        return

    def mostrar(self, vista):
        return