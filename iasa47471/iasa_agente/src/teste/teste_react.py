from control_react.ControloReact import ControloReact
from control_react.reaccoes.explorar.Explorar import Explorar
from sae import Simulador

controlo = ControloReact(Explorar())
Simulador(1, controlo).executar()