from mod.problema.Problema import Problema

# Esta classe representa um tipo de problema, especificando a classe Problema.
# Este problema recebe um modelo do planeamento e um estado final.
class ProblemaPlan(Problema):
    def __init__(self, modelo_plan, estado_final):
        self.estado_final = estado_final
        super().__init__(modelo_plan.estado, modelo_plan.operadores)

    # Objetivo do problema
    def objetivo(self, estado):
        # Return Boolean
        return
