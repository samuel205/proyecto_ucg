from strategies.base_strategy import EstrategiaAnalisis


class EstrategiaStress(EstrategiaAnalisis):

    def analizar(self, df):

        resultado = {
            "promedio_estres": round(df["stress_level"].mean(), 2),
            "max_estres": df["stress_level"].max(),
            "min_estres": df["stress_level"].min(),
            "promedio_ansiedad": round(df["anxiety_level"].mean(), 2),
        }

        return resultado
