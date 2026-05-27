class DatasetValidator:

    COLUMNAS_REQUERIDAS = [
        "age",
        "gender",
        "daily_social_media_hours",
        "platform_usage",
        "sleep_hours",
        "screen_time_before_sleep",
        "academic_performance",
        "physical_activity",
        "social_interaction_level",
        "stress_level",
        "anxiety_level",
        "addiction_level",
        "depression_label",
    ]

    @staticmethod
    def validar_columnas(df):

        columnas_faltantes = []

        for columna in DatasetValidator.COLUMNAS_REQUERIDAS:

            if columna not in df.columns:
                columnas_faltantes.append(columna)

        return columnas_faltantes
