import streamlit as st
import plotly.graph_objects as go


def render_digital_paradox(df):

    with st.container(border=True):

        st.subheader("The Digital Paradox")

        st.caption("""
            Correlation analysis of "Daily Social Media Hours"
            and "Anxiety Level" across the adolescent dataset.
            """)

        col_chart, col_info = st.columns([2.5, 1], gap="large")

        # ==========================
        # GRAFICO
        # ==========================

        with col_chart:

            df_chart = df[["daily_social_media_hours", "anxiety_level"]].reset_index()

            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=df_chart.index,
                    y=df_chart["daily_social_media_hours"],
                    mode="lines",
                    name="Social Media (Hrs)",
                    line=dict(width=4, shape="spline"),
                )
            )

            fig.add_trace(
                go.Scatter(
                    x=df_chart.index,
                    y=df_chart["anxiety_level"],
                    mode="lines",
                    name="Anxiety Level",
                    line=dict(width=4, dash="dot", shape="spline"),
                )
            )

            fig.update_layout(
                height=450,
                margin=dict(l=20, r=20, t=40, b=20),
                legend=dict(
                    orientation="h", yanchor="bottom", y=1.05, xanchor="right", x=1
                ),
                xaxis_title="",
                yaxis_title="",
            )

            st.plotly_chart(fig, use_container_width=True)

        # ==========================
        # NARRATIVA
        # ==========================

        with col_info:

            correlacion = round(
                df["daily_social_media_hours"].corr(df["anxiety_level"]), 2
            )

            st.info(f"""
                ### Key Narrative

                Correlación detectada:

                **{correlacion}**

                Existe relación entre el tiempo
                invertido en redes sociales y los
                niveles reportados de ansiedad.

                El nivel de interacción social puede
                actuar como un factor protector dentro
                del comportamiento académico.
                """)

            if st.button("Analyze Correlation Matrix"):

                st.dataframe(
                    df[
                        [
                            "daily_social_media_hours",
                            "sleep_hours",
                            "stress_level",
                            "anxiety_level",
                            "academic_performance",
                        ]
                    ].corr(),
                    use_container_width=True,
                )
