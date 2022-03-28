from sae.agente.controlo import Controlo

# Classe Controlo Reativo - extende a classe Controlo
# Recebe como parametro um comportamento
class ControloReact(Controlo):
    def __init__(self, comportamento):
        self._comportamento = comportamento

    # Processa a percepcao recebida a retorna
    # a ação a executar
    def processar(percepcao):
        accao = None
        return accao