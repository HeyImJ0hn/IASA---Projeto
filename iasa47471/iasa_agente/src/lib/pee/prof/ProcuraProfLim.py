from pee.prof.ProcuraProf import ProcuraProf

# Esta classe representa um mecanismo de procura, Procura em Profundidade Limitada.
# Extende a classe ProcuraProf.
# Esta procura limita a procura a uma profundidade máxima (por omissão é 1000)


class ProcuraProfLim(ProcuraProf):
    def resolver(self, problema, prof_max=1000):
        # guarda prof maxima e retorna resolver da superclasse
        self.prof_max = prof_max
        return super().resolver(problema)

    # Recebe um problema e um nó e executa o método "expandir" da classe
    # MecanismoProcura
    def _expandir(self, problema, no):
        # se a profundidade do nó for menor que a prof maxima
        if no.profundidade < self.prof_max:
            yield from super().expandir(problema, no)
        return
