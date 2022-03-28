from random import choice
from control_react.reaccoes.resposta.RespostaMover import RespostaMover
from ecr.IComportamento import IComportamento
from sae.ambiente.direccao import Direccao

# Classe Explorar - Implementa a interface IComportamento
# Representa um comportamento/sub-comportamento
# Este comportamento permite ao agente explorar 
# o ambiente em redor de forma aleatória. 
# É um sub-comportamento com menor 
# prioridade do comportamento "Recolher", ou seja,
# é o sub-comportamento ativado quando nenhum dos outros
# sub-comportamentos estão ativos.
class Explorar(IComportamento):

    # Recebe uma percepcao e ativa
    # o sub-comportamento "Explorar", retornando
    # a respetiva accao.
    # Isto é possível através do método "activar" da 
    # classe "Resposta". É criada uma instancia da classe
    # "RespostaMover", classe que extende "Resposta", e é usado
    # o método "activar" que retorna uma accao.
    def activar(self, percepcao):
        direccao = choice(list(Direccao))
        return RespostaMover(direccao).activar(percepcao)