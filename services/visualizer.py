import plotly.express as px


class Visualizer:

    @staticmethod
    def grafico_estres(df):

        fig = px.histogram(df, x="stress_level", title="Distribución de Estrés")

        return fig
