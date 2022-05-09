from mod.Estado import Estado

# Esta classe representa um tipo de estado, EstadoAgente.
# Este estado vai guardar uma posição entregue ao construtor e gerar
# um id único através do método "id_valor".

class EstadoAgente(Estado):
    def __init__(self, posicao):
        self.posicao = posicao

    # Gera um id único a patir da posição com a ajuda do método
    # do python "hash"
    def id_valor(self):
        return hash(self.posicao)
