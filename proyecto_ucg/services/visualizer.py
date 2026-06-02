import plotly.express as px


class Visualizer:

    @staticmethod
    def grafico_estres(df):

        fig = px.histogram(
            df, x="stress_level", title="Distribución del Nivel de Estrés"
        )

        return fig

    @staticmethod
    def grafico_rendimiento(df):

        fig = px.scatter(
            df,
            x="daily_social_media_hours",
            y="academic_performance",
            color="gender",
            title="Redes Sociales vs Rendimiento Académico",
        )

        return fig

    @staticmethod
    def grafico_ansiedad(df):

        fig = px.box(
            df,
            x="gender",
            y="anxiety_level",
            color="gender",
            title="Ansiedad por Género",
        )

        return fig
