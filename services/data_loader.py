import pandas as pd


class DataLoader:

    @staticmethod
    def cargar_dataset(path):
        return pd.read_csv(path)
