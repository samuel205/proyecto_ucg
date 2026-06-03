import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# ============================================
# COMPONENTE PRINCIPAL
# ============================================


def render_lifestyle_analysis(df):

    col1, col2 = st.columns(2, gap="large")

    render_activity(col1, df)

    render_sleep(col2, df)


# ============================================
# ACTIVIDAD FISICA
# ============================================


def render_activity(column, df):

    with column:

        with st.container(border=True):

            st.subheader("Physical Activity Impact 🏃")

            st.caption("Anxiety Recovery vs. Daily Exercise (hrs)")

            data = df.copy()

            # Crear rangos similares al diseño

            bins = [0, 0.5, 1, 1.5, 2, 10]

            labels = ["0h", "0.5h", "1.0h", "1.5h", "2.0h+"]

            data["activity_group"] = pd.cut(
                data["physical_activity"], bins=bins, labels=labels, include_lowest=True
            )

            resumen = (
                data.groupby("activity_group")["anxiety_level"].mean().reset_index()
            )

            # Mientras menos ansiedad mejor recuperación

            resumen["recovery_score"] = 10 - resumen["anxiety_level"]

            fig = go.Figure()

            fig.add_trace(
                go.Bar(
                    x=resumen["activity_group"],
                    y=resumen["recovery_score"],
                    text=round(resumen["recovery_score"], 1),
                    textposition="outside",
                )
            )

            fig.update_layout(
                height=350,
                showlegend=False,
                yaxis=dict(visible=False),
                xaxis=dict(title=""),
                margin=dict(l=20, r=20, t=20, b=20),
            )

            st.plotly_chart(fig, width='stretch')


# ============================================
# SUEÑO
# ============================================


def render_sleep(column, df):

    with column:

        with st.container(border=True):

            st.subheader("Sleep Duration Trends 🌙")

            st.caption("Mean nightly sleep hours distribution")

            sleep_mean = round(df.sleep_hours.mean(), 1)

            percentage = round((len(df[df.sleep_hours >= 8]) / len(df)) * 100)

            fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=sleep_mean,
                    number={"suffix": " h"},
                    gauge={"axis": {"range": [0, 10]}, "bar": {"thickness": 0.35}},
                )
            )

            fig.update_layout(height=300, margin=dict(l=30, r=30, t=20, b=20))

            st.plotly_chart(fig, width='stretch')

            if percentage >= 60:

                st.success(f"""
                    {percentage}% of students reach
                    recommended 8+ hours of sleep.
                    """)

            elif percentage >= 30:

                st.warning(f"""
                    Only {percentage}% reaches
                    recommended 8+ hours of sleep.
                    """)

            else:

                st.error(f"""
                    Only {percentage}% of the monitored
                    group reaches the recommended
                    8+ hours of sleep.
                    """)
