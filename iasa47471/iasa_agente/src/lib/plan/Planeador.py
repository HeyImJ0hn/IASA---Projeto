from abc import ABC, abstractmethod


class Planeador(ABC):
    def __init__(self):
        return

    def planear(self, modelo_mundo, objetivos):
        return

    def terminar_plano(self):
        pass

    def obter_accao(self, estado):
        return