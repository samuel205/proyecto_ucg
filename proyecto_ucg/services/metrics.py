class MetricsService:

    @staticmethod
    def total_estudiantes(df):
        return len(df)

    @staticmethod
    def promedio_estres(df):
        return round(df["stress_level"].mean(), 2)

    @staticmethod
    def promedio_rendimiento(df):
        return round(df["academic_performance"].mean(), 2)

    @staticmethod
    def promedio_ansiedad(df):
        return round(df["anxiety_level"].mean(), 2)
