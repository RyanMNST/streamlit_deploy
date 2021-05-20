# Dependencies and Libraries
from sklearn.utils import resample
import streamlit as st
import numpy as np
import pandas as pd
import sklearn as skl
import matplotlib as plt
import seaborn as sns
import pickle

# Classifer Library
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.metrics.pairwise import cosine_similarity
import category_encoders as ce

# Load learned model
# loaded_model = pickle.load(open('model.pkl', 'rb'))
# loaded_encoder = pickle.load(open('encoder.pkl', 'rb'))

# ============================================================
# Result Function : Random Forest Implementation
rf_classifier = RandomForestClassifier(n_estimators=100)
model = Pipeline
X_encoder = ce.OneHotEncoder(cols=[
        'Recent sexual activity',
        'Region',
        'Type of place of residence',
        'Current marital status',
        'Currently pregnant',
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
    ])

def predict():
    df = pd.read_csv('clean_data.csv')
    df = df.loc[df['Current contraceptive method'] != 'Not using']
    df['Current contraceptive method'] = df['Current contraceptive method'].replace('Calendar or rhythm method/Periodic abstinence', 'Periodic abstinence', regex=True)
    df['Current contraceptive method'] = df['Current contraceptive method'].replace('Implants/Norplant', 'Implants', regex=True)
    df['Current contraceptive method'] = df['Current contraceptive method'].replace('Mucus/Billing/Ovulation', 'Ovulation', regex=True)

    columns = ["Respondent's current age",
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
    X = df[columns]
    y = df['Current contraceptive method']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    X_train = X_encoder.fit_transform(X_train)
    X_test = X_encoder.transform(X_test)
    rf_classifier.fit(X_train, y_train)

    model = Pipeline([("preprocessing",X_encoder),("model",rf_classifier)]).fit(X_train, y_train)

st.write("""
# System Web Application Version
A [CS 321 | CS 322] Project
""")

with st.form("Counseling_Form"):
    # ============================================================
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


    # ============================================================
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


    # ============================================================
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


    # ============================================================
    # Status of Woman and Pregnancy Features
    st.markdown("**Status of Woman and Pregnancy Features**")
    swp_1 = st.selectbox(
        label="Current pregnancy status?", 
        options=[
            'Fecund', 
            'Postpartum Amenorrheic', 
            'Infecund, menopausal', 
            'Pregnant'
            ],
        index=0
    )

    swp_3_1, swp_2_1 = st.beta_columns(2)

    with swp_2_1:
        swp_2 = st.radio(
            label="Currently pregnant?",
            options=['Yes', 'No'],
            index=1
        )

    with swp_3_1:
        swp_3 = st.number_input(
            label="Total number of pregnancies",
            min_value=0,
        )


    # ============================================================
    # Recent Births Features
    st.markdown("**Recent Births Features**")
    rb_1 = st.selectbox(
        label="Current Marital Status", 
        options=[
            'Married', 
            'Widowed', 
            'No longer living together/separated', 
            'Divorced', 
            'Living with partner',
            'Never in union'
            ],
        index=0
    )

    rb_2_1, rb_3_1, rb_4_1 = st.beta_columns(3)

    with rb_2_1:
        rb_2 = st.number_input(
            label="Births in last five (5) years",
            min_value=0,
        )

    with rb_3_1:
        rb_3 = st.number_input(
            label="Births in last three (3) years",
            min_value=0,
        )

    with rb_4_1:
        rb_4 = st.number_input(
            label="Births in past year",
            min_value=0,
        )


    # ============================================================
    # Decision on Contraception Features
    st.markdown("**Decision on Contraception Features**")
    dc_1_1, dc_2_1 = st.beta_columns(2)

    with dc_1_1:
        dc_1 = st.selectbox(
            label="Decision maker for using a contraception", 
            options=[
                'Joint decision', 
                'None', 
                'Mainly husband, partner', 
                'Mainly respondent', 
                'Other'
                ],
            index=0
        )

    with dc_2_1:
        dc_2 = st.selectbox(
            label="Decision maker for not using a contraception",
            options=[
                'Joint decision', 
                'None', 
                'Mainly husband, partner', 
                'Mainly respondent', 
                'Other',
                ],
            index=0
        )

    dc_3 = st.selectbox(
        label="Preferred future contraception method",
        options=[
            'Not using', 
            'Pill', 
            'Implants/Norplant', 
            'IUD', 
            'Injections',
            'Female sterilization', 
            'Male condom', 
            'Withdrawal',
            'Sympothermal',
            'Other traditional method',
            'Calendar or rhythm method/Periodic abstinence', 
            'Patch',
            'Mucus/Billing/Ovulation', 
            'Basal Body temperature',
            'Other modern method', 
            'Male sterilization', 
            'Female condom',
            'Standard days method (SDM)',
            ],
        index=0
    )


    # ============================================================
    # Do you smoke/indulge in the following?
    st.markdown("**Vices Features**")

    vice_1_1, vice_2_1, vice_3_1 = st.beta_columns(3)

    with vice_1_1:
        vice_1 = st.radio(
            label="Do you use cigarettes?",
            options=['Yes', 'No'],
            index=1
        )

    with vice_2_1:
        vice_2 = st.radio(
            label="Do you snuff by nose?",
            options=['Yes', 'No'],
            index=1
        )

    with vice_3_1:
        vice_3 = st.radio(
            label="Do you smoke a water pipe?",
            options=['Yes', 'No'],
            index=1
        )

    vice_4_1, vice_5_1, vice_6_1 = st.beta_columns(3)

    with vice_4_1:
        vice_4 = st.radio(
            label="Do you smoke a tobacco pipe?",
            options=['Yes', 'No'],
            index=1
        )

    with vice_5_1:
        vice_5 = st.radio(
            label="Do you use kreteks?",
            options=['Yes', 'No'],
            index=1
        )

    with vice_6_1:
        vice_6 = st.radio(
            label="Do you snuff by mouth?",
            options=['Yes', 'No'],
            index=1
        )

    vice_7_1, vice_8_1, vice_9_1 = st.beta_columns(3)

    with vice_7_1:
        vice_7 = st.radio(
            label="Do you chew tobacco?",
            options=['Yes', 'No'],
            index=1
        )

    with vice_8_1:
        vice_8 = st.radio(
            label="Do you use cigars, cheroots, cigarillos?",
            options=['Yes', 'No'],
            index=1
        )

    with vice_9_1:
        vice_9 = st.radio(
            label="Do you chew betel quid with tobacco?",
            options=['Yes', 'No'],
            index=1
        )


    # ============================================================
    # Unmet Needs Features
    st.markdown("**Unmet Needs Features**")
    unmet_need_1 = st.selectbox(
        label="Unmet Need (1)", 
        options=[
            'Using for spacing', 
            'No unmet need', 
            '99', 
            'Using for limiting', 
            'Not married and no sex in last 30 days',
            'Unmet need for spacing', 
            'Infecund, menopausal', 
            'Unmet need for limiting'
            ],
        index=1
    )

    unmet_need_2 = st.selectbox(
        label="Unmet Need (2)",
        options=[
            'Using for spacing', 
            'No unmet need', 
            'Infecund, menopausal', 
            'Using for limiting',
            'Not married and no sex in last 30 days', 
            'Unmet need for spacing', 
            'Unmet need for limiting'
            ],
        index=1
    )

    unmet_need_3 = st.selectbox(
        label="Unmet Need (3)", 
        options=[
            'Using for spacing', 
            'No unmet need', 
            '99', 
            'Using for limiting', 
            'Not married and no sex in last 30 days',
            'Unmet need for spacing', 
            'Infecund, menopausal', 
            'Unmet need for limiting'
            ],
        index=1
    )

    submit_button = st.form_submit_button(label="Submit Information")
    if submit_button:
        st.write("Predicting/Recommending Contraceptive...")
        predict()

        user_df = pd.DataFrame({
            "Respondent's current age":[{current_age}],
            'Age of respondent at 1st birth':[{age_first_birth}],
            'Age at first menstrual period':[{age_first_period}],
            'Recent sexual activity':[{recent_sex_act}],
            'Region':[{residential_status}],
            'Type of place of residence':[{rural_area}],
            'Current marital status':[{rb_1}],
            'Births in last five years':[{rb_2}],
            'Births in last three years':[{rb_3}],
            'Births in past year':[{rb_4}],
            'Currently pregnant':[{swp_2}],
            'Total number all pregnacies':[{swp_3}],
            'Decision maker for using contraception':[{dc_1}],
            'Decision maker for not using contraception':[{dc_2}],
            'Preferred future method':[{dc_3}],
            'Smokes cigarettes':[{vice_1}],
            'Smokes pipe full of tobacco':[{vice_4}],
            'Chews tobacco':[{vice_7}],
            'Snuffs by nose':[{vice_2}],
            'Smokes kreteks':[{vice_5}],
            'Smokes cigars, cheroots or cigarillos':[{vice_8}],
            'Smokes water pipe':[{vice_3}],
            'Snuff by mouth':[{vice_6}],
            'Chews betel quid with tobacco':[{vice_9}],
            "Husband's desire for children":[{husband_desire}],
            'Exposure':[{swp_1}],
            'Unmet need':[{unmet_need_1}],
            'Unmet need (definition 2)':[{unmet_need_2}],
            'Unmet need for contraception (definition 3)':[{unmet_need_3}],
        })

        # user_encode = X_encoder.fit_transform(user_df)
        user_encode = model.predict(user_df)
        st.write(rf_classifier.predict(user_encode))
        



# ============================================================
# Show Result Function