from strategies.cleaning_strategy import EstrategiaLimpieza


class EstrategiaModa(EstrategiaLimpieza):

    def limpiar(self, serie):
        return serie.fillna(serie.mode()[0])
