import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from pathlib import Path


def read_data():
    m_path = Path(__file__).parent
    data_path = m_path.joinpath("dataset/clean_data.csv")
    df = pd.read_csv(data_path, index_col=0)
    df["Current contraceptive method"] = df["Current contraceptive method"].replace(
        "Calendar or rhythm method/Periodic abstinence", "Periodic abstinence", regex=True)
    df["Current contraceptive method"] = df["Current contraceptive method"].replace(
        "Implants/Norplant", "Implants", regex=True)
    df["Current contraceptive method"] = df["Current contraceptive method"].replace(
        "Mucus/Billing/Ovulation", "Ovulation", regex=True)

    df["Preferred future method"] = df["Preferred future method"].replace(
        "Calendar or rhythm method/Periodic abstinence", "Periodic abstinence", regex=True)
    df["Preferred future method"] = df["Preferred future method"].replace(
        "Implants/Norplant", "Implants", regex=True)
    df["Preferred future method"] = df["Preferred future method"].replace(
        "Mucus/Billing/Ovulation", "Ovulation", regex=True)
    return df


def pairplot(data, vars=None):
    if vars is None:
        vars = list(data.columns)

    chart = alt.Chart(data).mark_circle().encode(
        alt.X(alt.repeat("column"), type="quantitative"),
        alt.Y(alt.repeat("row"), type="quantitative"),
        color="Origin:N"
    ).properties(
        width=300,
        height=300
    ).repeat(
        row=vars,
        column=vars
    ).interactive()
    return chart


def app():
    st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 1200px;
        padding-top: 1rem;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 1rem;
    }}
    .reportview-container .main {{
        color: BLACK;
        background-color: WHITE;
    }}
</style>
""",
        unsafe_allow_html=True,
    )

    st.write("""
    # Finals System Web Application Version
    A [CS 321 | CS 322] Project - Dataset Dashboard
    """)

    data = read_data()

    st.markdown("**Random Sample of the dataset**")
    st.write(data.sample(n=25))

    features = ["Respondent's current age",
                "Age of respondent at 1st birth",
                "Age at first menstrual period",
                "Recent sexual activity",
                "Region",
                "Type of place of residence",
                "Current marital status",
                "Births in last five years",
                "Births in last three years",
                "Births in past year",
                "Currently pregnant",
                "Total number all pregnacies",
                "Current contraceptive method",
                "Decision maker for using contraception",
                "Decision maker for not using contraception",
                "Preferred future method",
                "Smokes cigarettes",
                "Smokes pipe full of tobacco",
                "Chews tobacco",
                "Snuffs by nose",
                "Smokes kreteks",
                "Smokes cigars, cheroots or cigarillos",
                "Smokes water pipe",
                "Snuff by mouth",
                "Chews betel quid with tobacco",
                "Husband's desire for children",
                "Exposure",
                "Unmet need",
                "Unmet need (definition 2)",
                "Unmet need for contraception (definition 3)"
                ]

    st.markdown("**Examine the dataset**")
    chosen_feature = st.selectbox(
        "Select the feature of the dataset to examine", tuple(features))
    col1, col2 = st.columns([1, 2])

    col1.write("Value Counts")
    feature_data = data[chosen_feature].value_counts()
    col1.dataframe(feature_data)

    col2.write("Chart")
    col2.bar_chart(data[chosen_feature].value_counts(), width=0, height=0)

    st.markdown('**Graphs from the Paper**')

    with st.form("Graphs"):
        pairplot_button = st.form_submit_button(
            label="Pair plot relationship (Age Features - Pregnancy Features)")
        heatmap_button = st.form_submit_button(
            label="Heatmap (Age Features - Pregnancy Features)")
        future_button = st.form_submit_button(
            label="Bar Graph (Preferred Future Method")
        residence_button = st.form_submit_button(
            label="Pie Chart (Type of Residence")

        if pairplot_button:
            graph = 'pairplot'
            img_path = f'https://raw.githubusercontent.com/RyanMNST/streamlit_deploy/main/graphs/{graph}.png'
            st.markdown(
                f"<img src='{img_path}' style='display: block; margin-left: auto; margin-right: auto; width: 100%;'>", unsafe_allow_html=True)

        elif heatmap_button:
            graph = 'heatmap'
            img_path = f'https://raw.githubusercontent.com/RyanMNST/streamlit_deploy/main/graphs/{graph}.png'
            st.markdown(
                f"<img src='{img_path}' style='display: block; margin-left: auto; margin-right: auto; width: 60%;'>", unsafe_allow_html=True)

        elif future_button:
            graph = 'future_method'
            img_path = f'https://raw.githubusercontent.com/RyanMNST/streamlit_deploy/main/graphs/{graph}.png'
            st.markdown(
                f"<img src='{img_path}' style='display: block; margin-left: auto; margin-right: auto; width: 60%;'>", unsafe_allow_html=True)

        elif residence_button:
            graph = 'type_of_residence'
            img_path = f'https://raw.githubusercontent.com/RyanMNST/streamlit_deploy/main/graphs/{graph}.png'
            st.markdown(
                f"<img src='{img_path}' style='display: block; margin-left: auto; margin-right: auto; width: 60%;'>", unsafe_allow_html=True)
