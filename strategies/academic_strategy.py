from strategies.base_strategy import EstrategiaAnalisis


class EstrategiaAcademica(EstrategiaAnalisis):

    def analizar(self, df):

        resultado = {
            "promedio_estudio": df["daily_social_media_hours"].mean(),
            "promedio_asistencia": df["academic_performance"].mean(),
        }

        return resultado
