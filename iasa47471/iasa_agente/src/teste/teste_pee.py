from controlo_delib.ControloDelib import ControloDelib
from plan_pee.PlanPEE import PlanPEE
from sae import Simulador
from plan_traj.Ligacao import Ligacao
from teste.plan_traj.PlaneadorTrajecto import PlaneadorTrajecto
from teste.plan_traj.mod_prob.OperadorLigacao import OperadorLigacao

# Esta classe é a classe que permite testar a procura
# em espaços de estados. É criada uma lista com ligações e este
# é entregue ao método "planear" da classe "PlaneadorTrajecto", assim como
# a localização inicial e final.

ligacoes = [
    OperadorLigacao('Loc-0', 'Loc-1', 5),
    OperadorLigacao('Loc-0', 'Loc-2', 25),
    OperadorLigacao('Loc-1', 'Loc-3', 12),
    OperadorLigacao('Loc-1', 'Loc-6', 5),
    OperadorLigacao('Loc-2', 'Loc-4', 30),
    OperadorLigacao('Loc-3', 'Loc-2', 10),
    OperadorLigacao('Loc-3', 'Loc-5', 5),
    OperadorLigacao('Loc-4', 'Loc-3', 2),
    OperadorLigacao('Loc-5', 'Loc-6', 8),
    OperadorLigacao('Loc-5', 'Loc-4', 10),
    OperadorLigacao('Loc-6', 'Loc-3', 15)
]

#planeador = PlaneadorTrajecto()
#solucao = planeador.planear(ligacoes, 'Loc-0', 'Loc-2')
#planeador.mostrar_trajecto(solucao)


planpee = PlanPEE()

controlo = ControloDelib(planpee)
Simulador(1, controlo).executar()
