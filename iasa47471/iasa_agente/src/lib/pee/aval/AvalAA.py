from pee.aval.AvalHeur import AvalHeur

# Esta classe representa uma avaliação de custo do tipo
# de procura A* (heurística admissível)
# Tem como objetivo uma minimização de custo global
#
# É possivel ser calculado através da fórumula:
# f(n) = g(n) + h(n)


class AvalAA(AvalHeur):
    def prioridade(self, no):
        return no.custo + self.heuristica.h(no.estado)
