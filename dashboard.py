import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

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


def app():
    st.write("""
    # Finals System Web Application Version
    A [CS 321 | CS 322] Project - Dataset Dashboard
    """)

    m_path = Path(__file__).parent
    data_path = m_path.joinpath('dataset/clean_data.csv')

    data = pd.read_csv(data_path, index_col=0)

    st.markdown("**Sample of the dataset**")
    st.write(data.head(25))

    features = ["Respondent's current age",
    'Age of respondent at 1st birth',
    'Age at first menstrual period',
    'Recent sexual activity',
    'Region',
    'Type of place of residence',
    'Current marital status',
    'Births in last five years',
    'Births in last three years',
    'Births in past year',
    'Currently pregnant',
    'Total number all pregnacies',
    'Decision maker for using contraception',
    'Decision maker for not using contraception',
    'Preferred future method',
    'Smokes cigarettes',
    'Smokes pipe full of tobacco',
    'Chews tobacco',
    'Snuffs by nose',
    'Smokes kreteks',
    'Smokes cigars, cheroots or cigarillos',
    'Smokes water pipe',
    'Snuff by mouth',
    'Chews betel quid with tobacco',
    "Husband's desire for children",
    'Exposure',
    'Unmet need',
    'Unmet need (definition 2)',
    'Unmet need for contraception (definition 3)'
    ]

    chosen_feature = st.selectbox("Select the feature of the dataset to examine", tuple(features))
    col1, col2 = st.beta_columns(2)

    col1.write('Unique Values')
    col1.write(data[chosen_feature].unique())
    # col1.write('Value Counts')
    # col1.write(data[chosen_feature].value_counts().sort_values(ascending=False))

    col2.write("Chart")
    col2.bar_chart(data[chosen_feature].value_counts(), width=500, height=500)