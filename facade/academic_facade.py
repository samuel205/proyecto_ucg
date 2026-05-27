from services.data_loader import DataLoader
from factory.analysis_factory import FabricaAnalisis


class FachadaAcademica:

    def __init__(self, uploaded_file):

        self.df = DataLoader.cargar_dataset(uploaded_file)

    def obtener_dataset(self):

        return self.df

    def ejecutar_analisis(self, tipo):

        estrategia = FabricaAnalisis.crear(tipo)

        return estrategia.analizar(self.df)
