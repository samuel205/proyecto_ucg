import streamlit as st


def render_sidebar(df):

    with st.sidebar:

        st.title("Dashboard")

        st.caption("Academic Insights & Digital Behavior Analysis")

        menu = st.radio("Navegación", ["Dashboard", "Dataset"])

        st.divider()

        # =========================
        # FILTERS
        # =========================

        st.markdown("""
            ### F I L T E R S
            """)

        st.write("")

        # =========================
        # Gender
        # =========================

        st.subheader("Gender")

        gender = st.selectbox(
            label="gender_filter",
            options=["All", "male", "female"],
            label_visibility="collapsed",
        )

        st.write("")

        # =========================
        # Platform
        # =========================

        st.subheader("Platform Usage")

        platform = st.selectbox(
            label="platform_filter",
            options=[
                "All",
                "Instagram",
                "TikTok",
                "Both",
            ],
            label_visibility="collapsed",
        )

        st.write("")

        # =========================
        # Social Interaction
        # =========================

        st.subheader("Social Interaction")

        low = st.checkbox("Low", value=True)

        medium = st.checkbox("Medium", value=True)

        high = st.checkbox("High", value=True)

        interaction = []

        if low:
            interaction.append("low")

        if medium:
            interaction.append("medium")

        if high:
            interaction.append("high")

        st.write("")

        # =========================
        # Age Range
        # =========================

        st.subheader("Age Range")

        age_option = st.segmented_control(
            label="age_filter",
            options=["All", "13-15", "16-18", "19+"],
            default="All",
            label_visibility="collapsed",
        )

    # =========================
    # APPLY FILTERS
    # FUERA DEL SIDEBAR
    # =========================

    df_filter = df.copy()

    if gender != "All":

        df_filter = df_filter[df_filter["gender"] == gender]

    if platform != "All":

        df_filter = df_filter[df_filter["platform_usage"] == platform]

    if interaction:

        df_filter = df_filter[df_filter["social_interaction_level"].isin(interaction)]

    if age_option == "13-15":

        df_filter = df_filter[(df_filter.age >= 13) & (df_filter.age <= 15)]

    elif age_option == "16-18":

        df_filter = df_filter[(df_filter.age >= 16) & (df_filter.age <= 18)]

    elif age_option == "19+":

        df_filter = df_filter[df_filter.age >= 19]

    return menu, df_filter
