from factory.cleaning_factory import FabricaLimpieza


class DataCleaner:

    COLUMNAS = [
        "daily_social_media_hours",
        "sleep_hours",
        "academic_performance",
        "stress_level",
        "anxiety_level",
        "addiction_level",
        "gender",
        "platform_usage",
        "social_interaction_level",
        "physical_activity",
        "depression_label",
    ]

    @classmethod
    def limpiar(cls, df):

        print("===== COLUMNAS =====")
        print(df.columns.tolist())

        print("===== NULOS =====")
        print(df.isna().sum())

        reporte = []

        for columna in cls.COLUMNAS:
            faltantes_antes = df[columna].isna().sum()
            estrategia = FabricaLimpieza.crear(columna)
            df[columna] = estrategia.limpiar(df[columna])

            reporte.append(
                {
                    "columna": columna,
                    "faltantes_antes": faltantes_antes,
                    "faltantes_despues": df[columna].isna().sum(),
                    "estrategia": (
                        estrategia.__class__.__name__
                        if faltantes_antes > 0
                        else "No requerida"
                    ),
                }
            )

        return df, reporte
