from sae import Controlo
from sae import Simulador

class ControloTeste(Controlo):
    def processar(self, percepcao):
        print("processar")

# Ativação do simulador
controlo = ControloTeste()
Simulador(1, controlo).executar()