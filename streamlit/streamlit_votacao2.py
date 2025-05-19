import streamlit as st

st.set_page_config(page_title="Votacao", layout="wide")

lista = [''] * 6
disciplinas = ["DDD", "CTP", "AI", "Frontend", "Database", "Software design"]

for i in range(len(lista)):
    lista[i] = st.checkbox(disciplinas[i])

col1, col2, col3 = st.columns(3)

with col1:
    for i in range(len(lista)):
        if lista[i]:
            st.slider(disciplinas[i], 0, 100)

