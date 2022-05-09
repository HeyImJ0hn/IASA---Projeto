from controlo_delib.ModeloMundo import ModeloMundo
from sae.agente.controlo import Controlo
from sae.ambiente.elemento import Elemento

# Esta classe representa o controlo de uma arquitetura deliberativa.
# O controlo deliberativo usa um raciocínio prático.
# Um raciocínio prático tem dois componentes: Raciocínio sobre fins (deliberação)
# e Raciocínio sobre meios (planeamento).
#
# O Raciocínio sobre fins tem opções para decidir o que fazer e o
# resultado deste raciocínio vão ser objetivos, ou seja, quando é feita uma
# deliberação são produzidos objetivos.
# O Raciocínio sobre meios tem ações para decidir como fazer e o
# resultado são planos, ou seja, quando é feito um planeamento são
# gerados planos.
#
# O raciocínio prático tem alguns problemas, como os recursos computacionais
# e o dinamismo do ambiente, ou seja, a memória e o tempo de computação
# não são ilimitados, e o ambiente pode mudar durante o raciocínio, o que causa uma
# inconsistencia com a situação do ambiente. Para resolver isto é feita uma
# reavaliação de opções e uma eventual mudança de planos.
# O processo de tomada de decisão passa a ter um passo extra, "Reconsiderar" que
# verifica então se o mundo está sincronizado. O processo passa então a ser:
# Oberservar o mundo, atualizar crenças, é feita a reconsideração e caso esteja sincronizado
# é feita a deliberação e depois um planeamento. Por fim é executado o plano de ação.
#
# A esta classe é entregue um planeador. No construtor vai ser guardado este planeador e 
# criado um modelo do tipo "ModeloMundo", bem como criada uma lista de objetivos, que começa vazia.

class ControloDelib(Controlo):
    def __init__(self, planeador):
        self._planeador = planeador
        self._modelo = ModeloMundo()
        self._objetivos = []

    # Vai iniciar todo o processo de tomada de decisão
    # Com a percepcao recebida é entregue ao método "assimilar" que vai atualizar
    # o modelo mundo. É feita então uma reconsideração para verificar se o modelo foi
    # alterado ou não.
    # Se sim são corridos os métodos "deliberar" e "planear" que cria objetivos
    # a partir dos estados no modelo e gera ou termina um plano, sucessivamente.
    # No fim de tudo, quer o modelo tenha sido alterado ou não, é executado o plano.
    def processar(self, percepcao):
        self._assimilar(percepcao)
        if self._reconsiderar():
            self._deliberar()
            self._planear()
        return self._executar()

    # Atualiza o modelo mundo
    def _assimilar(self, per):
        self._modelo.actualizar(per)

    # Lidar com o facto do tempo de processamento nao ser 0
    # Usado como mecanismo de sincronização com o mundo
    # Verifica se o que tem que ser feito está de acordo com o mundo
    def _reconsiderar(self):
        return self._modelo.alterado()

    # Atualiza os objetivos com uma lista de estados que tem o estado por
    # cada posicao que tem um alvo
    def _deliberar(self):
        self._objetivos = [estado for estado in self._modelo.estados()
                            if self._modelo.obter_elem(estado) == Elemento.ALVO]

    # Método planear(modelo, objetivos) - gera um plano
    # Método terminar_plano() - cancela o plano
    #
    # É feita uma verificação para saber se existem objetivos.
    # Caso existam é gerado um novo plano. Caso contrário, 
    # é terminado o plano.
    def _planear(self):
        if not self._objetivos:
            self._planeador.terminar_plano()
        else:
            self._planeador.planear(self._modelo, self._objetivos)

    # obter_accao(estado) - retorna operador que representa a ação a executar nesse estado
    # ^ se nao existir plano ou se nao existir operador retorna None
    def _executar(self):
        return self._planeador.obter_accao(self._modelo.estado())

    # Permite mostrar todo o modelo e o plano no visor.
    def _mostrar(self):
        self.vista.limpar()
        self._modelo.mostrar()
        self._planeador.mostrar(self.vista)
        self.__vista.mostrar_estados(self._objetivos)