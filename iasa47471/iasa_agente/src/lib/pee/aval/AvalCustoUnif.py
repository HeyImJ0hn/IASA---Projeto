from pee.aval.Avaliador import Avaliador

# Esta classe representa uma avaliação de custo do tipo
# de procura de custo uniforme
# Esta avaliação nao tira partido de conhecimento do
# domínio do problema expresso através da função h(n), ou seja,
# função heurística, ao contrário dos outros avaliadores.
# Tem uma avaliação baseada no custo e este pode ser calculado
# através da seguinte expressão:
# f(n) = g(n)


class AvalCustoUnif(Avaliador):
    def prioridade(self, no):
        return no.custo
