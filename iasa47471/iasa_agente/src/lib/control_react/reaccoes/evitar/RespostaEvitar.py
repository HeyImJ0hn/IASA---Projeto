from random import choice
from control_react.reaccoes.resposta.RespostaMover import RespostaMover
from sae.ambiente.direccao import Direccao

# Classe RespostaEvitar - Extende a classe RespostaMover
# Esta classe vai contribuir para o funcionamento da arquitetura
# reactiva de memória.
# Instanciada na classe "EvitarObst" esta classe vai ajudar na
# gestão de direccoes livres.


class RespostaEvitar(RespostaMover):
    # Neste construtor, inicialmente é chamado o construtor da superclasse,
    # entregando a direccao inicial.
    # A dir_inicial é o unico argumento deste construtor e caso não seja
    # entregue, a dir_inicial é ESTE.
    # No construtor é ainda criada uma lista de direccoes com todas as direccoes
    # no enum "Direccao".
    def __init__(self, dir_inicial=Direccao.ESTE):
        super().__init__(dir_inicial)
        self.direccao = dir_inicial
        self._direccoes = list(Direccao)

    # O método activar serve para activar a resposta na direccao
    # necessária, ou seja, mover o agente na direccao pretendida
    # através do método "activar" da superclasse "RespostaMover".
    # Inicialmente é feita uma verificação para saber se o agente
    # teve algum contacto com um obstáculo. Para isto é usado o método
    # "contacto_obst" da classe "Percepcao". Caso haja algum contacto
    # com um obstáculo, é feita outra verificação. Esta verificação consiste
    # em usar o método "direccao_livre" para obter alguma direccao livre em
    # redor do agente e é guardada numa variável com o mesmo nome.
    # Se existir alguma direccao livre para onde o agente possa andar é
    # alterada a propriedade da direçao (self.accao.direccao) para a nova
    # direccao livre aleatória e é mudada a variável anteriormente definida
    # de contacto com um obstáculo para False. Esta mudança é feita para
    # simplificar o código, pois na primeira verificação, caso não haja nenhum
    # contacto com um obstáculo é chamado o método "activar" da superclasse e
    # o agente mexe na direccao atual. A variável é então mudada por este motivo,
    # pois nós queremos que seja lido esse código depois de ser atualizada a
    # direccao do agente.
    def activar(self, percepcao, intensidade):
        contacto_obst = percepcao.contacto_obst(self.accao.direccao)
        if contacto_obst:
            direccao_livre = self.direccao_livre(percepcao)
            if direccao_livre:
                self.accao.direccao = direccao_livre
                contacto_obst = False
        if not contacto_obst:
            super().activar(percepcao, intensidade)

    # Este método vai verificar se existe alguma direccao
    # livre à volta do agente.
    # Através do método contacto_obst da percepcao entregue como
    # argumento é possível fazer um for loop para verificar se
    # alguma das direccoes em redor não tem um obstáculo.
    # Este loop vai encher uma lista de direccoes livres (dir_livres)
    # que vai conter então todas as direccoes sem nenhum obstáculo.
    # No fim da função é retornada uma direção random. Isto é possível
    # através do método "choice" do módulo "Random", que recebe a lista
    # e retorna um dos elementos escolhido ao acaso.
    def direccao_livre(self, percepcao):
        dir_livres = [direccao for direccao in self._direccoes
                      if not percepcao.contacto_obst(direccao)]
        return choice(dir_livres)
