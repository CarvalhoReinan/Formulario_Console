import streamlit as st
from config import frameworks, horas, estudo, nivel

st.title("Formulário de Estudos em Python 🐍")

st.expander("Sobre o Formulário", expanded=True).markdown("Este formulário é uma forma divertida de coletar informações sobre como você estuda Python.")
st.sidebar.header("Configurações")
pagina = st.sidebar.selectbox("Selecione a página", ["Formulário Principal", "Sobre o Formulário"])
if pagina == "Sobre o Formulário":
    st.sidebar.markdown("""
    Este formulário foi criado para entender melhor como as pessoas estudam Python.
    Ele coleta informações sobre o nível de conhecimento, frameworks utilizados e métodos de estudo.
    """)
elif pagina == "Formulário Principal":
    st.sidebar.markdown("""
    Preencha o formulário abaixo para compartilhar como você estuda Python.
    Suas respostas nos ajudarão a entender melhor a comunidade de desenvolvedores Python.
    """)
nome = st.text_input("Qual seu nome?")
nome = nome.strip().capitalize()  # Remove espaços e capitaliza o nome
if nome:
    nivel_escolhido = st.selectbox(f"{nome}, qual seu nível em Python?", nivel)

    if nivel_escolhido == "Avançado":
        framework = st.selectbox(f"{nome}, você usa algum framework?", frameworks)
        if framework == "Outro?":
            outro = st.text_input("Qual outro framework você usa?")
            if outro:
                st.success(f"Legal! Você usa {outro}.")
        elif framework != "Cancelar":
            st.success(f"Muito bom! Você está usando {framework}.")
    
    metodo = st.selectbox("Por onde você estuda Python?", estudo)
    if metodo == "Outro?":
        outro_metodo = st.text_input("Qual o método que você usa?")
        if outro_metodo:
            st.info(f"Você estuda por: {outro_metodo}")

    tempo = st.selectbox("Quanto tempo você estuda por dia?", horas)
    if tempo == "Mais de 4 Horas":
        outros = st.text_input("Quantas horas exatamente?")
        if outros:
            st.success(f"{outros} horas! Muito bom!")
    elif tempo:
        st.success(f"Tempo selecionado: {tempo}")

envio = st.button("Enviar Respostas")
if envio: 
        st.success(f"{nome}, obrigado por enviar suas respostas!")
    