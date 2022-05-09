# Esta classe representa uma solução do método de procura.

class Solucao:
    def __init__(self, no_final):
        self.percurso = []
        no = no_final
        while no:
            self.percurso.insert(0, no)
            no = no.antecessor

    # Remover o primeiro passo do percurso
    def remover_passo(self):
        self.percurso.pop(0)

    def __iter__(self):
        return iter(self.percurso)

    def __getitem__(self, index):
        return self.percurso[index]
