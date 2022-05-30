from pee.aval.AvalCustoUnif import AvalCustoUnif
from pee.melhor_prim.ProcuraMelhorPrim import ProcuraMelhorPrim

# Procura de Custo Uniforme é um mecanismo de procura. Extende a classe procura Melhor-Primeiro.
# A estratégia de controlo desta procura é explorar primeiro os caminhos com menor custo
# e custo de transição >= E > 0

# Não tira partido de conhecimento do domínio do problema
# expresso através da função h(n)
# f(n) = g(n)


class ProcuraCustoUnif(ProcuraMelhorPrim):

    # Este método vai iniciar o Avaliador de Custo Uniforme
    def _iniciar_avaliador():
        return AvalCustoUnif()
