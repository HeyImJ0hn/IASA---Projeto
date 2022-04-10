from control_react.reaccoes.aproximar.AproximarAlvo import AproximarAlvo
from control_react.reaccoes.evitar.EvitarObst import EvitarObst
from control_react.reaccoes.explorar.Explorar import Explorar
from ecr.Hierarquia import Hierarquia

# Classe Recolher - Extende a classe Hierarquia.
# Representa um dos objetivos do agente.
# A classe recolher vai usar a Hierarquia como
# método de selecção de acção.
# Este comportamento é o comportamento principal do agente.
# É composto por 3 comportamentos, ou sub-objetivos, sendo estes
# AproximarAlvo, EvitarObst e Explorar.
# Como foi referido antes, este comportamento vai utilizar o método
# de seleccao das accoes "Hierarquia". Neste caso a prioridade do agente
# é aproximar-se do alvo, através da classe AproximarAlvo, de seguida a prioridade
# é evitar os obstáculos, através da classe EvitarObst, e por fim, caso nenhum dos
# outros dois comportamentos esteja ativo, o agente segue o comportamento Explorar,
# através da classe Explorar.


class Recolher(Hierarquia):
    # Neste construtor é criada uma lista de comportamentos com os 3
    # comportamentos referidos anteriormente, AproximarAlvo, EvitarObst
    # e Explorar.
    # Esta lista é então entregue ao construtor da superclasse "Hierarquia"
    # que vai tratar de selecionar o comportamento com a maior prioridade,
    # neste caso AproximarAlvo, seguido de EvitarObst e por fim Explorar.
    def __init__(self):
        comportamentos = [AproximarAlvo(), EvitarObst(), Explorar()]
        super().__init__(comportamentos)
