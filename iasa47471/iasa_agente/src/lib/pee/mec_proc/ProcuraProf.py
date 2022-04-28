from pee.mec_proc.MecanismoProcura import MecanismoProcura

# Esta classe representa um mecanismo de procura em profundidade (depth-first search).
# Nesta procura a estratégia de controlo é explorar primeiro os 
# nós mais recentes.

class ProcuraProf(MecanismoProcura):
    def _iniciar_fronteira(self):
        # Retorna Fronteira
        return

    def _memorizar(self, no):
        return