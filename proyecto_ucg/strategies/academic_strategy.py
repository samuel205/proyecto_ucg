from strategies.base_strategy import EstrategiaAnalisis


class EstrategiaAcademica(EstrategiaAnalisis):

    def analizar(self, df):

        resultado = {
            "promedio_rendimiento": round(df["academic_performance"].mean(), 2),
            "promedio_sueno": round(df["sleep_hours"].mean(), 2),
            "promedio_uso_redes": round(df["daily_social_media_hours"].mean(), 2),
        }

        return resultado
