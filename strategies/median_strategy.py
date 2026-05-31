from strategies.cleaning_strategy import EstrategiaLimpieza


class EstrategiaMediana(EstrategiaLimpieza):

    def limpiar(self, serie):
        return serie.fillna(serie.median())
