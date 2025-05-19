import streamlit as st

st.set_page_config(page_title="Votação", layout="wide")

opcao = st.radio("Disciplina que deseja avaliar: ",
                 ["CTP", "DDD", "Database", "Frontent", "AI", "System Design"])
nota = st.slider(opcao, 0, 100)

botao = st.button("Votar")

if botao:
    st.write(f"Você avaliou a disciplina {opcao} com a nota {nota}")