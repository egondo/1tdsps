import streamlit as st

st.set_page_config(page_title="Streamlit components", layout="wide")

nome = st.text_input("Nome: ")
idade = st.number_input("Idade: ", min_value=0, max_value=120)

st.write(f"Seu nome é {nome} e vc tem {idade} anos")

instrucao = st.selectbox("Instrução", ["fundamental", "médio", "superior", "pós-graduação"])

esportes = st.multiselect("Quais esportes você já praticou", ["futebol", "vôlei", "basquete", "handebol", "tênis", "judô", "outros"])
st.write(f"Grau de instrução: {instrucao}")
st.write(f"Esportes: {esportes}")

if "outros" in esportes:
    outros_esportes = st.text_input("Quais os outros esportes? ")
    st.write(outros_esportes)
