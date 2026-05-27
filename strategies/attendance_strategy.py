from strategies.base_strategy import EstrategiaAnalisis


class EstrategiaAsistencia(EstrategiaAnalisis):

    def analizar(self, df):

        estudiantes_riesgo = df[
            (df["stress_level"] >= 8) & (df["academic_performance"] <= 2.5)
        ]

        return {"estudiantes_riesgo": len(estudiantes_riesgo)}
