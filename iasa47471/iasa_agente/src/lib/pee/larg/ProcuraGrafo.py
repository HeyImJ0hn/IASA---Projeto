from pee.mec_proc.MecanismoProcura import MecanismoProcura

# Esta classe representa um mecanismo de procura em grafos.
# Nesta procura os nós abertos são gerados mas não expandidos e
# os nós fechados são nós expandidos.


class ProcuraGrafo(MecanismoProcura):
    # O método resolver vai então executar o mecanismo explicado em cima.
    def resolver(self, problema):
        # dicionario com estado e nó
        self.explorados = {}
        return super().resolver(problema)

    def _memorizar(self, no):
        if self._manter(no):
            # adicionar aos explorados
            self.explorados[no.estado.localidade] = no
            self.fronteira.inserir(no)


    def _manter(self, no):
        if no not in self.explorados:
            return True
