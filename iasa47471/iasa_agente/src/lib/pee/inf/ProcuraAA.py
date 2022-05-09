from pee.aval.AvalAA import AvalAA
from pee.inf.ProcuraInformada import ProcuraInformada

# Esta classe representa a procura A*, ou AA. A procura A* é um
# tipo de procura informada.
# Esta procura tem heurística admissível, logo 0 <= h(n) <= h*(n).
# Uma heurística admissível é obtida através da remoção de restrições
# associadas ao problema, por exemplo: Navegação autónoma. Na distância
# de Manhattan isto corresponde a retirar a restrição de não se poder
# movimentar através dos obstáculos. Na distância Euclidiana isto corresponde
# a retirar também a impossibilidade de movimentação através de obstáculos
# mas também a não movimentação em diagonal.
# Uma heurística admissível é também otimista. A estimativa de custo é sempre
# inferior ou igual ao custo mínimo.
#
# Este método de procura é completo e ótimo.


class ProcuraAA(ProcuraInformada):
    def iniciar_avaliador(self):
        return AvalAA(self.heuristica)
