from dataclasses import dataclass

from mod.Estado import Estado
from mod.IOperador import IOperador

@dataclass
class PassoSolucao:
    estado: Estado
    operador: IOperador