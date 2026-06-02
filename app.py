import streamlit as st

from facade.academic_facade import FachadaAcademica

from components.sidebar import render_sidebar
from components.dashboard import render_dashboard

st.set_page_config(page_title="UCG", layout="wide")


uploaded_file = st.file_uploader("Subir dataset CSV", type=["csv"])


if uploaded_file is None:

    st.warning("Debe cargar un dataset para iniciar")

    st.stop()


fachada = FachadaAcademica(uploaded_file)


df = fachada.obtener_dataset()


menu, df_filter = render_sidebar(df)


if menu == "Dashboard":

    render_dashboard(df_filter)


elif menu == "Dataset":

    st.dataframe(df_filter, width='stretch')
