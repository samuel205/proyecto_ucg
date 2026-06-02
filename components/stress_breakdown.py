import streamlit as st
import plotly.graph_objects as go
import pandas as pd


def render_stress_breakdown(df):

    with st.container(border=True):

        st.subheader("Stress Level Demographic Breakdown")

        st.caption("Mean Stress Level (0-10) by Age Group and Gender")

        # ==========================
        # Crear grupos de edad
        # ==========================

        data = df.copy()

        def grupo_edad(age):

            if age <= 15:
                return "Ages 13-15"

            elif age <= 18:
                return "Ages 16-18"

            return "Ages 19+"

        data["age_group"] = data["age"].apply(grupo_edad)

        # ==========================
        # Agrupar datos
        # ==========================

        resumen = (
            data.groupby(["age_group", "gender"])["stress_level"].mean().reset_index()
        )

        orden = ["Ages 13-15", "Ages 16-18", "Ages 19+"]

        male = []

        female = []

        for grupo in orden:

            male_value = resumen[
                (resumen.age_group == grupo) & (resumen.gender == "male")
            ]

            female_value = resumen[
                (resumen.age_group == grupo) & (resumen.gender == "female")
            ]

            male.append(
                round(male_value.stress_level.values[0], 1)
                if not male_value.empty
                else 0
            )

            female.append(
                round(female_value.stress_level.values[0], 1)
                if not female_value.empty
                else 0
            )

        # ==========================
        # Crear gráfica
        # ==========================

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                y=orden,
                x=male,
                name="Male",
                orientation="h",
                text=male,
                textposition="outside",
            )
        )

        fig.add_trace(
            go.Bar(
                y=orden,
                x=female,
                name="Female",
                orientation="h",
                text=female,
                textposition="outside",
            )
        )

        fig.update_layout(
            height=420,
            barmode="group",
            xaxis=dict(range=[0, 10], visible=False),
            yaxis=dict(autorange="reversed"),
            legend=dict(
                orientation="h", yanchor="bottom", y=1.05, xanchor="right", x=1
            ),
            margin=dict(l=20, r=40, t=40, b=20),
        )

        st.plotly_chart(fig, use_container_width=True)
