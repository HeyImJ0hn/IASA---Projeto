from pee import Fronteira

# Representa um tipo de fronteira, Fronteira First In First Out.

class FronteiraFIFO(Fronteira):

    # Insere um nó na lista de nos definida na superclasse Fronteira
    def inserir(self, no):
        self.nos.append(no)