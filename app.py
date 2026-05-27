import streamlit as st

from facade.academic_facade import FachadaAcademica
from services.metrics import MetricsService
from services.visualizer import Visualizer

# CONFIG
st.set_page_config(page_title="Academic Insight AI", layout="wide")

# TITULO
st.title("Academic Insight AI")

# FACHADA
fachada = FachadaAcademica("data/Teen_Mental_Health_Dataset.csv")

# DATASET
df = fachada.obtener_dataset()

# SIDEBAR
menu = st.sidebar.selectbox(
    "Seleccione análisis", ["Dashboard", "Stress", "Academico", "Asistencia"]
)

# DASHBOARD
if menu == "Dashboard":

    st.subheader("KPIs")

    col1, col2 = st.columns(2)

    col1.metric("Total Estudiantes", MetricsService.total_estudiantes(df))

    col2.metric("Promedio Estrés", MetricsService.promedio_estres(df))

    fig = Visualizer.grafico_estres(df)

    st.plotly_chart(fig)

# STRESS
elif menu == "Stress":

    resultado = fachada.ejecutar_analisis("stress")

    st.write(resultado)

# ACADEMICO
elif menu == "Academico":

    resultado = fachada.ejecutar_analisis("academico")

    st.write(resultado)

# ASISTENCIA
elif menu == "Asistencia":

    resultado = fachada.ejecutar_analisis("asistencia")

    st.write(resultado)
