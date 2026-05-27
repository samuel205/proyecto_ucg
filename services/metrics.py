class MetricsService:

    @staticmethod
    def total_estudiantes(df):
        return len(df)

    @staticmethod
    def promedio_estres(df):
        return round(df["stress_level"].mean(), 2)
