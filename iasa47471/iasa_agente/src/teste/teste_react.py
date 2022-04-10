from control_react.ControloReact import ControloReact
from control_react.reaccoes.Recolher import Recolher
from sae import Simulador

# Esta classe é uma classe de testes que tem como objetivo
# testar a arquitetura reativa do agente.
# É criada uma instância da classe ControloReact e entregue o comportamento
# Recolher.
# É depois, através da classe Simulador, executado este comportamento
controlo = ControloReact(Recolher())
Simulador(1, controlo).executar()
