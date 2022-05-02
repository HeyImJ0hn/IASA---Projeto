from dataclasses import dataclass

# Dataclass de uma ligação
@dataclass
class Ligacao:
    origem: str
    destino: str
    custo: int