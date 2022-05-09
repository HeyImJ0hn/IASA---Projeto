from dataclasses import dataclass

# Esta classe é uma dataclass e tem como objetivo representar
# uma ligação que vai desde a origem ao destino e comtém
# também o seu respetivo custo.


@dataclass
class Ligacao:
    origem: str
    destino: str
    custo: int
