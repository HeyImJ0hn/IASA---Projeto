from mod.Estado import Estado

# Tal como o Estado, o EstadoLocalidade representa uma configuração de um
# sistema ou de um problema e tem tabém uma identificação única (id)


class EstadoLocalidade(Estado):
    def __init__(self, localidade):
        self.localidade = localidade

    def id_valor(self):
        return self.localidade.__hash__()
