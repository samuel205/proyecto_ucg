import streamlit as st

from facade.academic_facade import FachadaAcademica
from services.metrics import MetricsService
from services.visualizer import Visualizer
from services.validator import DatasetValidator

# CONFIG
st.set_page_config(page_title="Academic Insight AI", layout="wide")

# TITULO
st.title("Academic Insight AI")

st.markdown("""
Sistema inteligente para análisis de bienestar
emocional y rendimiento académico estudiantil.
""")

# ==========================
# CARGA DE ARCHIVO
# ==========================

uploaded_file = st.file_uploader("Cargue un archivo CSV", type=["csv"])

# SI NO HAY ARCHIVO
if uploaded_file is None:

    st.warning("""
    Debe cargar un archivo CSV para continuar.
    """)

    st.stop()

# ==========================
# CREAR FACHADA
# ==========================

fachada = FachadaAcademica(uploaded_file)

df = fachada.obtener_dataset()

# ==========================
# VALIDAR COLUMNAS
# ==========================

columnas_faltantes = DatasetValidator.validar_columnas(df)

if len(columnas_faltantes) > 0:

    st.error("El dataset no contiene las columnas requeridas.")

    st.write("Columnas faltantes:")

    st.write(columnas_faltantes)

    st.stop()

# ==========================
# DATASET CORRECTO
# ==========================

st.success("Dataset cargado correctamente.")

# ==========================
# SIDEBAR
# ==========================

menu = st.sidebar.selectbox(
    "Seleccione módulo", ["Dashboard", "Stress", "Academico", "Riesgo"]
)

# ==========================
# DASHBOARD
# ==========================

if menu == "Dashboard":

    st.subheader("Indicadores Principales")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Estudiantes", MetricsService.total_estudiantes(df))

    col2.metric("Promedio Estrés", MetricsService.promedio_estres(df))

    col3.metric("Promedio Ansiedad", MetricsService.promedio_ansiedad(df))

    st.plotly_chart(Visualizer.grafico_estres(df), use_container_width=True)

    st.plotly_chart(Visualizer.grafico_rendimiento(df), use_container_width=True)

# ==========================
# STRESS
# ==========================

elif menu == "Stress":

    st.subheader("Análisis de Estrés")

    resultado = fachada.ejecutar_analisis("stress")

    st.json(resultado)

    st.plotly_chart(Visualizer.grafico_estres(df), use_container_width=True)

# ==========================
# ACADEMICO
# ==========================

elif menu == "Academico":

    st.subheader("Análisis Académico")

    resultado = fachada.ejecutar_analisis("academico")

    st.json(resultado)

    st.plotly_chart(Visualizer.grafico_rendimiento(df), use_container_width=True)

# ==========================
# RIESGO
# ==========================

elif menu == "Riesgo":

    st.subheader("Estudiantes en Riesgo")

    resultado = fachada.ejecutar_analisis("asistencia")

    st.json(resultado)

    st.plotly_chart(Visualizer.grafico_ansiedad(df), use_container_width=True)

# ==========================
# VISTA DEL DATASET
# ==========================

st.subheader("Vista previa del dataset")

st.dataframe(df.head())
