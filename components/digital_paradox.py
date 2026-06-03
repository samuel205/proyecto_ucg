import streamlit as st
import plotly.express as px


def render_digital_paradox(df):

    with st.container(border=True):

        st.subheader("The Digital Paradox")

        st.caption("""
            Correlation analysis of "Daily Social Media Hours"
            and "Anxiety Level" across the adolescent dataset.
            """)

        col_chart, col_info = st.columns([2.5, 1], gap="large")

        # ==========================================
        # GRAFICO DE CORRELACION
        # ==========================================

        with col_chart:

            fig = px.scatter(
                df,
                x="daily_social_media_hours",
                y="anxiety_level",
                color="social_interaction_level",
                size="stress_level",
                trendline="ols",
                opacity=0.55,
                labels={
                    "daily_social_media_hours": "Daily Social Media (hrs)",
                    "anxiety_level": "Anxiety Level",
                    "social_interaction_level": "Social Interaction",
                    "stress_level": "Stress Level",
                },
            )

            fig.update_traces(marker=dict(size=9, line=dict(width=0.5)))

            fig.update_layout(
                height=450,
                legend=dict(
                    orientation="h", yanchor="bottom", y=1.05, xanchor="right", x=1
                ),
                margin=dict(l=20, r=20, t=40, b=20),
                xaxis=dict(showgrid=True),
                yaxis=dict(showgrid=True),
            )

            st.plotly_chart(fig, width='stretch')

        # ==========================================
        # PANEL NARRATIVO
        # ==========================================

        with col_info:

            correlacion = round(
                df["daily_social_media_hours"].corr(df["anxiety_level"]), 2
            )

            # ==========================
            # ANALISIS AUTOMATICO
            # ==========================

            if abs(correlacion) >= 0.7:

                estado = "Alta"

                mensaje = """
                Existe una relación fuerte entre el uso
                de redes sociales y los niveles de ansiedad.
                """

                alerta = "error"

            elif abs(correlacion) >= 0.3:

                estado = "Moderada"

                mensaje = """
                Existe una relación moderada.
                El uso digital podría influir parcialmente
                en la ansiedad.
                """

                alerta = "warning"

            else:

                estado = "Baja"

                mensaje = """
                No existe una correlación significativa.
                Otros factores como sueño, estrés y actividad
                física pueden tener mayor influencia.
                """

                alerta = "info"

            texto = f"""

            ### Key Narrative


            **Correlación detectada:**


            ## {correlacion}


            Nivel:

            **{estado}**


            {mensaje}


            La interacción social puede actuar como
            un factor protector dentro del comportamiento
            académico del estudiante.
            """

            if alerta == "error":

                st.error(texto)

            elif alerta == "warning":

                st.warning(texto)

            else:

                st.info(texto)

            # =====================================
            # MATRIZ DE CORRELACION
            # =====================================

            with st.expander("Analyze Correlation Matrix"):

                columnas = [
                    "daily_social_media_hours",
                    "sleep_hours",
                    "screen_time_before_sleep",
                    "stress_level",
                    "anxiety_level",
                    "addiction_level",
                    "academic_performance",
                ]

                matriz = df[columnas].corr().round(2)

                st.dataframe(matriz, width='stretch')

                fig_corr = px.imshow(matriz, text_auto=True, aspect="auto")

                st.plotly_chart(fig_corr, width='stretch')
