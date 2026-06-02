import streamlit as st

# =========================
# Estado dinámico
# =========================


def evaluar_estado(tipo, valor):

    if tipo == "social":

        if valor <= 3:
            return "Bueno", "green"

        elif valor <= 6:
            return "Regular", "orange"

        return "Alto uso", "red"

    elif tipo == "sleep":

        if valor >= 8:
            return "Excelente descanso", "green"

        elif valor >= 6:
            return "Descanso regular", "orange"

        return "Poco descanso", "red"

    elif tipo == "stress":

        if valor <= 3:
            return "Estrés bajo", "green"

        elif valor <= 7:
            return "Estrés moderado", "orange"

        return "Estrés alto", "red"

    elif tipo == "wellbeing":

        if valor >= 70:
            return "Saludable", "green"

        elif valor >= 40:
            return "En observación", "orange"

        return "Riesgo elevado", "red"
    return "Desconocido", "gray"


# =========================
# CARD
# =========================


def render_card(column, title, value, estado, color):

    with column:

        with st.container(border=True, height=120):

            st.caption(title)

            st.metric(label="", value=value, label_visibility="collapsed")


# =========================
# CARDS PRINCIPALES
# =========================


def metric_cards(df):

    col1, col2, col3, col4 = st.columns(4, gap="large")

    social = round(df.daily_social_media_hours.mean(), 1)

    sleep = round(df.sleep_hours.mean(), 1)

    stress = round(df.stress_level.mean(), 1)

    wellbeing = round(100 - (df.stress_level.mean() * 4 + df.anxiety_level.mean() * 3))

    estado, color = evaluar_estado("social", social)

    render_card(col1, "Avg. Daily Social Media", f"{social} hrs/day", estado, color)

    estado, color = evaluar_estado("sleep", sleep)

    render_card(col2, "Avg. Sleep Quality", f"{sleep} hrs/night", estado, color)

    estado, color = evaluar_estado("stress", stress)

    render_card(col3, "Mean Stress Level", f"{stress}/10", estado, color)

    estado, color = evaluar_estado("wellbeing", wellbeing)

    render_card(col4, "Wellbeing Score", f"{wellbeing}", estado, color)
