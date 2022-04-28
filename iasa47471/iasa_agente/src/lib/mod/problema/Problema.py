from abc import ABC, abstractmethod

# Esta classe representa um problema.
# Um problema é composto por um estado, que representa uma
# configuração na resolução de um problema e tem uma 
# indentificação única, e também um operador de transição de estado,
# que representa uma ação ou transformação de estado.

class Problema(ABC):
    # O construtor desta classe recebe o estado inicial e os operadores
    # para a transformação deste estado.
    def __init__(self, estado_inicial, operadores):
        self.estado_inicial = estado_inicial
        self.operadores = operadores

    # Este método abstrato vai retornar um boolean e tem como
    # argumento o estado.
    @abstractmethod
    def objectivo(estado):
        pass