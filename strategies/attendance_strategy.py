from strategies.base_strategy import EstrategiaAnalisis


class EstrategiaAsistencia(EstrategiaAnalisis):

    def analizar(self, df):

        estudiantes_riesgo = df[df["academic_performance"] < 70]

        return {"cantidad_riesgo": len(estudiantes_riesgo)}
