from strategies.mean_strategy import EstrategiaMedia
from strategies.median_strategy import EstrategiaMediana
from strategies.mode_strategy import EstrategiaModa
from strategies.zero_strategy import EstrategiaCero
import pandas as pd


class FabricaLimpieza:

    @staticmethod
    def crear(columna):
        if pd.api.types.is_numeric_dtype(columna):
            return EstrategiaMediana()
        else:
            return EstrategiaModa()
