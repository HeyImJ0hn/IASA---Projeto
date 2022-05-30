# Esta classe representa Processos de Decisão Markov.
# Para representar o mundo sob a forma de PDM são necessárias
# algumas coisas, como o conjunto de estados do mundo (S), 
# o conjunto de ações possíveis no estado "s" (sendo que "s" está contido em S),
# a probabilidade de transição de "s" para "s'" através de "a" (T), a recompensa
# esperada na transição de "s" para s' através de "a" (R), a taxa de desconto
# para recompensas diferidas no tempo e o tempo discreto (t).
#
# A Utilidade é a função do efeito cumulaivo da evolução da situação. Necessita da
# história de evolução (h), que é uma sequência de estados com ganhos ou perdas, e também
# a recompensa (R), que é o ganho ou perda num determinado estado e pode ser um valor finito
# positivo ou negativo.
# Estas recompensas podem ser recompensas aditivas ou recompensas descontadas no tempo. Este
# último tipo de recompensas requer um fator de desconto (taxa de desconto referida anteriormente)
# que pode ser um valor entre 0 e 1, e não estão limitadas a uma gama finita de valores.

class PDM():
    # Recebe um ModeloPDM, gama e delta_max.
    def __init__(self, modelo, gama, delta_max):
        self._modelo = modelo
        self._gama = gama
        self._delta_max = delta_max

    @property
    def gama(self):
        return self._gama

    @property
    def delta_max(self):
        return self._delta_max

    # Associa a cada escala um valor real e 
    # representa a utilidade de um determinado estado.
    def utilidade(self): 
        delta_max, S, A = self._delta_max, self._modelo.S, self._modelo.A
        U = {s: 0 for s in S()}
        while True:
            Uant = U.copy()
            delta = 0
            for s in S():
                U[s] = max([self.util_accao(s, a, Uant) for a in A(s)], default = 0)
                delta = max(delta, abs(U[s] - Uant[s]))
            if delta <= delta_max:
                break
        return U

    
    def util_accao(self, s, a, U):
        gama, T, R = self._gama, self._modelo.T, self._modelo.R
        return sum(p * (R(s, a, sn) + gama * U[sn]) for (p, sn) in T(s, a))

    # Função de politica óptima.
    # Gera uma politica de ação.
    # Função que indica para cada estado qual a ação a ser realizada
    def politica(self, U):
        S, A = self._delta_max, self._modelo.S, self._modelo.A
        pol = {}
        for s in S():
            pol[s] = max(A(s), key=lambda a: self.util_accao(s, a, U))
        return pol

    # Método principal do processo. Retorna  os valores dos Processos de Decisão.
    def resolver(self):
        return self.utilidade(), self.politica(self.utilidade)