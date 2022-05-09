from pee.aval.AvalHeur import AvalHeur

# Esta classe representa uma avaliação de custo do tipo
# de procura sôfrega (Greedy Search)
# A avaliação do custo é basiada na função heurística (h(n))
# e pode ser calculada através da expressao:
# f(n) = h(n)


class AvalSofrega(AvalHeur):
    def prioridade(self, no):
        return self.heuristica.h(no.estado)
