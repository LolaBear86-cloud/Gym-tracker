import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Gym Tracker", layout="wide")

if "logs" not in st.session_state:
    st.session_state.logs = []

st.title("Gym Progression Tracker")

day = st.selectbox("Day", ["Monday","Tuesday","Wednesday","Friday","Saturday"])
session = st.selectbox("Session", ["AM","PM"])

exercise = st.text_input("Exercise")

col1,col2,col3 = st.columns(3)
with col1:
    weight = st.number_input("Weight",0.0)
with col2:
    reps = st.number_input("Reps",0)
with col3:
    sets = st.number_input("Sets",0)

notes = st.text_input("Notes")

if st.button("Save"):
    st.session_state.logs.append({
        "date":str(date.today()),
        "day":day,
        "session":session,
        "exercise":exercise,
        "weight":weight,
        "reps":reps,
        "sets":sets,
        "notes":notes
    })

if st.session_state.logs:
    df = pd.DataFrame(st.session_state.logs)
    st.dataframe(df)
