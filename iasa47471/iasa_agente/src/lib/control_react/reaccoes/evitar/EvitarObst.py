from control_react.reaccoes.evitar.EvitarDir import EvitarDir
from control_react.reaccoes.evitar.RespostaEvitar import RespostaEvitar
from ecr.Hierarquia import Hierarquia
from sae.ambiente.direccao import Direccao

# Classe EvitarObst - Extende a classe Hierarquia.
# Representa um dos objetivos do agente.
# A classe EvitarObst vai usar a Hierarquia como
# método de selecção de acção.
# Este comportamento, assim como os comportamentos Explorar
# e AproximarAlvo, fazem parte de um maior comportamento, ou objetivo,
# "Recolher".
# Este comportamento vai permitir ao agente evitar um obstáculo
# caso entre em contacto com o mesmo.


class EvitarObst(Hierarquia):
    # No construtor é criada uma única instancia da classe "RespostaEvitar"
    # e uma lista de instancias da classe "EvitarDir" com direccoes
    # diferentes mas sempre a mesma resposta.
    # Estes argumentos sao entregues no construtor da superclasse.
    def __init__(self):
        resposta_evitar = RespostaEvitar()
        super().__init__([EvitarDir(direccao, resposta_evitar)
                          for direccao in Direccao])
