from pee.larg.ProcuraLarg import ProcuraLarg
from pee.prof.ProcuraProf import ProcuraProf
from pee.prof.ProcuraProfLim import ProcuraProfLim
from teste.plan_traj.mod_prob.ProblemaPlanTraj import ProblemaPlanTraj

# Esta classe permite planear um trajeto desde a origem até ao final
# através do mecanismo de procura escolhido.


class PlaneadorTrajecto:
    # Este método recebe um conjunto de ligações, assim como uma localização
    # inicial e uma final. Com a ajuda de um mecanismo de procura é possível
    # resolver o problema criado através da classe "ProblemaPlanTraj".
    def planear(self, ligacoes, loc_inicial, loc_final):
        # Retorna Solucao
        problema = ProblemaPlanTraj(ligacoes, loc_inicial, loc_final)
        # Inicializar um mecanismo de procura
        #procura = ProcuraProf()
        solucao = ProcuraProf().resolver(problema)
        #return procura.resolver(problema)
        return solucao

    def mostrar_trajecto(self, solucao):
        for no in solucao.percurso:
            print(no.estado.localidade)
