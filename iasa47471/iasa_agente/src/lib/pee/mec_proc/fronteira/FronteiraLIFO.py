from pee import Fronteira

# Representa um tipo de fronteira, Fronteira Last In First Out.

class FronteiraLIFO(Fronteira):
    
    # Insere um nó na lista de nos definida na superclasse Fronteira
    def inserir(self, no):
        self.nos.append(no)