from control_react.reaccoes.evitar.EstimuloObst import EstimuloObst
from ecr.Reaccao import Reaccao

# Classe EvitarDir - Extende Reaccao.
# Esta classe permite ao agente
# evitar uma direccao por onde ja passou.
# Serve para associacar o estimulo obstaculo e a RespostaEvitar.
# Esta classe vai contribuir para a construção de uma
# arquitetura reactiva de memória.
# A arquitetura reactiva de memória vai resolver vários problemas
# face à arquitetura sem memória, como a falta de necessidade de evitar
# o passado, a possibilidade de o agente ficar preso num canto e
# comportamentos cíclicos.


class EvitarDir(Reaccao):
    # Entrega no construtor da superclasse uma instancia da classe
    # EstimuloObst, usando "direccao" como argumento, e
    # "resposta" do tipo RespostaEvitar entregue
    #  inicialmente ao construtor desta classe.
    def __init__(self, direccao, resposta):
        super().__init__(EstimuloObst(direccao), resposta)
