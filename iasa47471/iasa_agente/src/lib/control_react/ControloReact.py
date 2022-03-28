from sae.agente.controlo import Controlo

# Classe Controlo Reativo - extende a classe Controlo.
# Recebe como parametro um comportamento.
# Ativa também a processao direcional no construtor.
# O controlo reativo é uma forma controlo 
# do agente que implementa uma arquitetura reativa, ou seja,
# implementa esquemas comportamentais reativos,
# que usam comportamentos simples ou compostos
class ControloReact(Controlo):
    def __init__(self, comportamento):
        self._comportamento = comportamento
        self.mostrar_per_dir = True

    # Processa a percepcao recebida a retorna
    # a ação a executar através do método
    # "activar" do comportamento entregue inicialmente
    # na criação da instância da classe.
    def processar(self, percepcao):
        return self._comportamento.activar(percepcao)