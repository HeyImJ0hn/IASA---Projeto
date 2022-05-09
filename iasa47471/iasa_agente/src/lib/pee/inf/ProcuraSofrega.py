from pee.aval.AvalSofrega import AvalSofrega
from pee.inf.ProcuraInformada import ProcuraInformada

# Esta classe representa um tipo de procura informada,
# a Procura Sôfrega (Greedy Search).
# Este tipo de procura não tem em conta o custo do percurso explorado
# e tem como objetivo a minimização de custo local.
# Tem soluções sub-óptimas (problema dos óptimos locais) e o custo
# pode ser calculado através da expressão:
# f(n) = h(n)
#
# Esta procura, assim como a procura A*, tira partido do conhecimento
# do domínio do problema expresso através da função heurística (h(n)).


class ProcuraSofrega(ProcuraInformada):
    def iniciar_avaliador(self):
        return AvalSofrega(self.heuristica)
