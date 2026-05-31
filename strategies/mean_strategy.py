from strategies.cleaning_strategy import EstrategiaLimpieza


class EstrategiaMedia(EstrategiaLimpieza):

    def limpiar(self, serie):
        return serie.fillna(serie.mean())
