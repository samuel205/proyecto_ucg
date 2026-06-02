from strategies.mean_strategy import EstrategiaMedia
from strategies.median_strategy import EstrategiaMediana
from strategies.mode_strategy import EstrategiaModa
from strategies.zero_strategy import EstrategiaCero


class FabricaLimpieza:

    @staticmethod
    def crear(tipo):

        if tipo == "media":
            return EstrategiaMedia()

        elif tipo == "mediana":
            return EstrategiaMediana()

        elif tipo == "moda":
            return EstrategiaModa()

        elif tipo == "cero":
            return EstrategiaCero()

        raise ValueError("Estrategia no soportada")
