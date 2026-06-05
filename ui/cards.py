import streamlit as st

# =========================
# CARD
# =========================


def render_card(column, title, value):

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


    render_card(col1, "Avg. Daily Social Media", f"{social} hrs/day")

    render_card(col2, "Avg. Sleep Quality", f"{sleep} hrs/night")

    render_card(col3, "Mean Stress Level", f"{stress}/10")

    render_card(col4, "Wellbeing Score", f"{wellbeing}")
