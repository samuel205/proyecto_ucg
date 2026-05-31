from abc import ABC, abstractmethod


class EstrategiaLimpieza(ABC):

    @abstractmethod
    def limpiar(self, serie):
        pass
