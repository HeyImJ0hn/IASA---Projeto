from pee.larg.ProcuraGrafo import ProcuraGrafo
from pee.mec_proc.fronteira.FronteiraFIFO import FronteiraFIFO

# Esta classe representa um mecanismo de procura em largura (breadth-first search).
# Nesta procura a estratégia de controlo é explorar primeiro
# os nós mais antigos.


class ProcuraLarg(ProcuraGrafo):
    # Cria uma instancia da fronteira necessária para este tipo de mecanismo,
    # neste caso a fronteira FIFO
    def _iniciar_fronteira(self):
        return FronteiraFIFO()
