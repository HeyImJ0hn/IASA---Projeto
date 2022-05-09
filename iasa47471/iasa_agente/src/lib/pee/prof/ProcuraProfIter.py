from unittest import result
from pee.prof.ProcuraProfLim import ProcuraProfLim

# Representa outro mecanismo de procura, Procura em Profundidade Iterativa.
# Extende a classe ProcuraProfLim.
# Esta procura vai expandir os nós até encontrar uma solução


class ProcuraProfIter(ProcuraProfLim):
    def resolver(self, problema, inc_prof=1, prof_max=1000):
        for prof in range(0, prof_max, inc_prof):
            resultado = super().resolver(problema, prof)
            if resultado != "cutoff":
                return resultado
