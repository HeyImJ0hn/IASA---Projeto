from pee.Solucao import Solucao
from pee.mec_proc.MecanismoProcura import MecanismoProcura
from pee.mec_proc.No import No

# Esta classe representa um mecanismo de procura em grafos.
# Nesta procura os nós abertos são gerados mas não expandidos e
# os nós fechados são nós expandidos.

class ProcuraGrafo(MecanismoProcura):
    # O método resolver vai então executar o mecanismo explicado em cima.
    def resolver(self, problema):
        no = No(problema.estado_inicial)

        if problema.objectivo(no.estado):
            return Solucao(no)

        explorados = {problema.estado_inicial}

        while not self.fronteira.vazia():
            no = self.fronteira.remover()
            for child in self.expandir(problema, no):
                s = child.estado
                if problema.objectivo(s): return child
                if s not in explorados:
                    explorados.add(s)
                    self.fronteira.inserir(child)
        return "failure"

    def _memorizar(no):
        return super()._memorizar()

    def _manter(no):
        return