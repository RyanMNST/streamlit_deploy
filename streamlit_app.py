# Dependencies and Libraries
import streamlit as st
import numpy as np
import pandas as pd
import sklearn as skl
import matplotlib as plt
import seaborn as sns

st.write("""
# System Web Application Version
A [CS 321 | CS 322] Project
""")

# Residential Status Features
st.markdown("**Residential Status Features**")
rs_1, rs_2 = st.beta_columns(2)

with rs_1:
    residential_status = st.selectbox(
    label="Region", 
    options=[
        'Autonomous Region in Muslim Mindanao',
        'Bicol', 
        'Cagayan Valley',
        'Calabarzon',
        'Caraga',
        'Central Luzon',
        'Central Visayas', 
        'Cordillera', 
        'Davao',
        'Eastern Visayas', 
        'Ilocos', 
        'Mimaropa',
        'National Capital', 
        'Northern Mindanao', 
        'Soccskargen', 
        'Western Visayas', 
        'Zamboanga Peninsula', 
        ],
    index=7
    )

with rs_2:
    rural_area = st.selectbox(
    label="Area",
    options=[
        'Rural',
        'Urban'
    ],
    index=1
)


# Age Features
st.markdown("**Age Features**")
a_1, a_2, a_3 = st.beta_columns(3)

with a_1:
    current_age = st.number_input(
    label="Current Age",
    min_value=15,
    max_value=49,
)

with a_2:
    age_first_birth = st.number_input(
    label="Age at First Birth",
    min_value=15,
    max_value=49,
)

with a_3:
    age_first_period = st.number_input(
    label="Age at First Menstrual Period",
    min_value=15,
    max_value=49,
)

# Sexual Activity Information Features
st.markdown("**Sexual Activity Information Features**")
recent_sex_act = st.selectbox(
    label="Recent Sexual Activity", 
    options=[
        'Active in last 4 weeks', 
        'Not active in last 4 weeks - not postpartum abstinence',
        'Not active in last 4 weeks - postpartum abstinence'
        ],
    index=0
)

husband_desire = st.selectbox(
    label="Husband's Desire for Children",
    options=[
        "Both want same",
        "No desire",
        "Husband wants more",
        "Don't know",
        "Husband wants fewer",
        ],
    index=0
)