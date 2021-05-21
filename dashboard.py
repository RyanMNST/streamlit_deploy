import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from pathlib import Path

@st.cache(allow_output_mutation=True)
def read_data():
    m_path = Path(__file__).parent
    data_path = m_path.joinpath("dataset/clean_data.csv")
    df = pd.read_csv(data_path, index_col=0)
    df["Current contraceptive method"] = df["Current contraceptive method"].replace("Calendar or rhythm method/Periodic abstinence", "Periodic abstinence", regex=True)
    df["Current contraceptive method"] = df["Current contraceptive method"].replace("Implants/Norplant", "Implants", regex=True)
    df["Current contraceptive method"] = df["Current contraceptive method"].replace("Mucus/Billing/Ovulation", "Ovulation", regex=True)

    df["Preferred future method"] = df["Preferred future method"].replace("Calendar or rhythm method/Periodic abstinence", "Periodic abstinence", regex=True)
    df["Preferred future method"] = df["Preferred future method"].replace("Implants/Norplant", "Implants", regex=True)
    df["Preferred future method"] = df["Preferred future method"].replace("Mucus/Billing/Ovulation", "Ovulation", regex=True)
    return df

def pairplot(data, vars=None):
    if vars is None:
        vars = list(data.columns)

    chart = alt.Chart(data).mark_circle().encode(
                alt.X(alt.repeat("column"), type="quantitative"),
                alt.Y(alt.repeat("row"), type="quantitative"),
                color="Origin:N"
            ).properties(
                width=250,
                height=250
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

    features = ["Respondent\'s current age",
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

    examine_expander = st.beta_expander(label="Examine the Dataset")
    with examine_expander:
        col1, col2 = st.beta_columns(2)

        chosen_feature = col1.selectbox("Select the feature of the dataset to examine", tuple(features))
        col1.write("Value Counts")
        col1.write(data[chosen_feature].value_counts().sort_index(ascending=True))

        col2.write("Chart")
        col2.bar_chart(data[chosen_feature].value_counts(), width=0, height=0)

    paper_expander = st.beta_expander(label="Graphs from the Paper")
    with paper_expander:
        with st.form("Graphs"):
            for column_name in data.columns:
                if data[column_name].dtypes == np.object:
                    data[column_name] = data[column_name].astype("category")
                    data[column_name] = data[column_name].cat.codes
                    data[column_name] = data[column_name].astype(int)

            col1, col2 = st.beta_columns(2)

            pairplot_button = col1.form_submit_button(label="Pair plot relationship (Age Features - Pregnancy Features)")
            heatmap = col1.form_submit_button(label="Heatmap (Age - Maternal History)")

            if pairplot_button:
                col2.altair_chart(
                    pairplot(data, vars=["Respondent\\'s current age", "Age at first sex","Age of respondent at 1st birth","Total number all pregnacies","Births in last five years","Births in last three years","Births in past year"])
                )