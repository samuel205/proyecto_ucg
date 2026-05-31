from factory.cleaning_factory import FabricaLimpieza


class DataCleaner:

    COLUMNAS_MEDIA = ["daily_social_media_hours", "sleep_hours", "academic_performance"]

    COLUMNAS_MEDIANA = ["stress_level", "anxiety_level", "addiction_level"]

    COLUMNAS_MODA = ["gender", "platform_usage", "social_interaction_level"]

    COLUMNAS_CERO = ["physical_activity", "depression_label"]

    @classmethod
    def limpiar(cls, df):

        reporte = []

        for columna in df.columns:

            faltantes_antes = df[columna].isna().sum()

            if faltantes_antes == 0:
                continue

            if columna in cls.COLUMNAS_MEDIA:

                estrategia = FabricaLimpieza.crear("media")

            elif columna in cls.COLUMNAS_MEDIANA:

                estrategia = FabricaLimpieza.crear("mediana")

            elif columna in cls.COLUMNAS_MODA:

                estrategia = FabricaLimpieza.crear("moda")

            elif columna in cls.COLUMNAS_CERO:

                estrategia = FabricaLimpieza.crear("cero")

            else:
                estrategia = FabricaLimpieza.crear("moda")

            df[columna] = estrategia.limpiar(df[columna])

            reporte.append(
                {
                    "columna": columna,
                    "faltantes_antes": faltantes_antes,
                    "faltantes_despues": df[columna].isna().sum(),
                    "estrategia": estrategia.__class__.__name__,
                }
            )

        return df, reporte
