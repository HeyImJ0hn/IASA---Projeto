from pee.mec_proc.MecanismoProcura import MecanismoProcura
from pee.mec_proc.fronteira.FronteiraLIFO import FronteiraLIFO

# Esta classe representa um mecanismo de procura em profundidade (depth-first search).
# Nesta procura a estratégia de controlo é explorar primeiro os
# nós mais recentes.


class ProcuraProf(MecanismoProcura):
    def _iniciar_fronteira(self):
        return FronteiraLIFO()

    def _memorizar(self, no):
        self.fronteira.inserir(no)
