from services.data_loader import DataLoader
from factory.analysis_factory import FabricaAnalisis


class FachadaAcademica:

    def __init__(self, path_dataset):

        self.df = DataLoader.cargar_dataset(path_dataset)

    def obtener_dataset(self):
        return self.df

    def ejecutar_analisis(self, tipo):

        estrategia = FabricaAnalisis.crear(tipo)

        return estrategia.analizar(self.df)
