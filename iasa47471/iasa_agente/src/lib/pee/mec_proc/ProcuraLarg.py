from pee.mec_proc.ProcuraGrafo import ProcuraGrafo

# Esta classe representa um mecanismo de procura em largura (breadth-first search).
# Nesta procura a estratégia de controlo é explorar primeiro 
# os nós mais antigos.

class ProcuraLarg(ProcuraGrafo):
    def _iniciar_fronteira():
        return