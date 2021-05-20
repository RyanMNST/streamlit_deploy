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

# Residential Status
residential_status = st.selectbox(
    label="Region", 
    options=[
        'Autonomous Region in Muslim Mindanao', 
        'Zamboanga Peninsula', 
        'Soccskargen', 
        'Cordillera', 
        'Caraga',
        'National Capital', 
        'Western Visayas', 
        'Central Visayas', 
        'Ilocos', 
        'Cagayan Valley', 
        'Central Luzon',
        'Calabarzon', 
        'Mimaropa', 
        'Bicol', 
        'Eastern Visayas', 
        'Northern Mindanao', 
        'Davao'
        ],
    index=0
    )