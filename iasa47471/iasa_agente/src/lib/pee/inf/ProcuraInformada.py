from pee.melhor_prim.ProcuraMelhorPrim import ProcuraMelhorPrim

# Esta classe representa um método de procura informada.
# Esta procura é uma alternativa à procura custo uniforme.
# Um método de procura informada, ao contrário dos métodos de procura
# não informada, é uma procura guiada e seletiva.
# As estratégias de exploração do espaço de estados tiram partido de
# conhecimento do domínio do problema no sentido de ordenar a fronteira
# de exploração.


class ProcuraInformada(ProcuraMelhorPrim):
    def resolver(self, problema, heuristica):
        self.heuristica = heuristica
        return super().resolver(problema)
