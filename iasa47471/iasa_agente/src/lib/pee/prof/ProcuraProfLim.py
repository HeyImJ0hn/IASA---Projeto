from pee.Solucao import Solucao
from pee.mec_proc.No import No
from pee.prof.ProcuraProf import ProcuraProf

# Esta classe representa um mecanismo de procura, Procura em Profundidade Limitada.
# Extende a classe ProcuraProf.
# Esta procura limita a procura a uma profundidade máxima (por omissão é 1000)

class ProcuraProfLim(ProcuraProf):
    def resolver(self, problema, prof_max=1000):
        self.fronteira.inserir(No(problema.estado_inicial))
        self.resultado = "failure"

        while not self.fronteira.vazia():
            no = self.fronteira.remover()
            if problema.objectivo(no.estado):
                return Solucao(no)
            if no.profundidade > prof_max:
                resultado = "cutoff"
            else:
                for child in self.expandir(problema, no):
                    self.fronteira.inserir(child)
        return resultado

    # Recebe um problema e um nó e executa o método "expandir" da classe
    # MecanismoProcura
    def _expandir(self, problema, no):
        return super().expandir(problema, no)