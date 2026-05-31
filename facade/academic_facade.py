from services.data_loader import DataLoader
from factory.analysis_factory import FabricaAnalisis
from services.cleaner import DataCleaner


class FachadaAcademica:

    def __init__(self, uploaded_file):

        self.df = DataLoader.cargar_dataset(uploaded_file)
        self.df, self.reporte_limpieza = DataCleaner.limpiar(self.df)

    def obtener_dataset(self):

        return self.df

    def obtener_reporte_limpieza(self):
        return self.reporte_limpieza

    def ejecutar_analisis(self, tipo):

        estrategia = FabricaAnalisis.crear(tipo)

        return estrategia.analizar(self.df)
