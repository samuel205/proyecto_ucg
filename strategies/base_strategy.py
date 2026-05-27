from abc import ABC, abstractmethod


class EstrategiaAnalisis(ABC):

    @abstractmethod
    def analizar(self, df):
        pass
