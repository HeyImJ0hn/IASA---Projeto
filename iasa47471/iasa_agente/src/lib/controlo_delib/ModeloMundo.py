
from controlo_delib.OperadorMover import OperadorMover
from mod.agente.EstadoAgente import EstadoAgente
from plan.ModeloPlan import ModeloPlan
from sae.ambiente.direccao import Direccao

# Esta classe representa um modelo do mundo.
# Este modelo corresponde a um ambiente simulado, com vários elementos e estados.
# Este modelo tem vários atributos, um boolean alterado, um dicionário de elementos,
# um estado, uma lista de estados e uma lista de operadores.
# O boolean alterado vai permitir a outras classes verificar se o modelo foi alterado
# quando foi feita um atualizção ou não.
# O dicionário de elementos contém vários elementos, que podem ser acedidos através da sua posição.
# O estado corresponde ao estado atual do modelo.
# A lista de estados contém todos os estados contidos no modelo.
# A lista de operadores contém operadores do tipo OperadorMover para cada direção.
class ModeloMundo(ModeloPlan):
    def __init__(self):
        self._alterado = False
        self._elementos = {}
        self._estado = None
        self._estados = []
        self._operadores = [OperadorMover(self, direccao)
                            for direccao in Direccao]

    @property
    def alterado(self):
        return self._alterado

    @property
    def elementos(self):
        return self._elementos

    # Este método permite atualizar o modelo de acordo com a percepcao
    # Vai atualizar, caso necessário, a lista de elementos e estados
    # do ModeloMundo.
    # É criado um estado do tipo EstadoAgente com a posição da percepcao.
    # De seguida é verificado se os elementos da percepcao correspondem aos
    # elementos do modelo. Se sim, nada é alterado. Se não, é atualizado o dicionário
    # de elementos do mundo para os elementos da percepcao e é atualizada a lista de estados
    # com novos estados de acordo com a posição de cada elemento.
    # O boolean "alterado" é True ou False consoante tenha sido feita alguma alteração ou não.
    def actualizar(self, percepcao):
        self._estado = EstadoAgente(percepcao.posicao)
        if percepcao.elementos != self._elementos:
            self._elementos = percepcao.elementos
            self._estados = [EstadoAgente(posicao)
                            for posicao in percepcao.elementos]
            self._alterado = True
        else:
            self._alterado = False

    # Retorna o estado do modelo
    def estado(self):
        return self._estado

    # Retorna a lista de estados do modelo
    def estados(self):
        return self._estados

    # Retorna a lista de operadores do modelo
    def operadores(self):
        return self._operadores

    # Retorna o elemento do dicionário de elementos que corresponde
    # à posição do estado entregue
    def obter_elem(self, estado):
        return self._elementos.get(estado.posicao)

    # Mostra o modelo no visor
    def mostrar(self, vista):
        vista.mostrar_alvos_obst(self._elementos)
        vista.marcar_posicao(self._estado.posicao)
