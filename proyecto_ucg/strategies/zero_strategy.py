from strategies.cleaning_strategy import EstrategiaLimpieza


class EstrategiaCero(EstrategiaLimpieza):

    def limpiar(self, serie):
        return serie.fillna(0)
