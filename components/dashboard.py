import streamlit as st
import plotly.express as px

from components.cards import metric_cards
from components.digital_paradox import render_digital_paradox
from components.stress_breakdown import render_stress_breakdown
from components.lifestyle_analysis import render_lifestyle_analysis


def render_dashboard(df):

    st.title("Dashboard")

    metric_cards(df)

    st.write("")

    render_digital_paradox(df)

    render_stress_breakdown(df)

    render_lifestyle_analysis(df)
