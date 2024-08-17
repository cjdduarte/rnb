import streamlit as st
import random
import os

# Forçar o modo de produção
os.environ["STREAMLIT_GLOBAL_DEVELOPMENT_MODE"] = "false"

# Configurações da página
st.set_page_config(
    page_title="Gerador de Número Aleatório",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# Ocultar menu de hambúrguer, rodapé e botão Deploy
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .center-number {
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        color: #FF4B4B;
    }
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Título do aplicativo
st.title("Gerador de Número Aleatório")

# Campos de entrada de texto
min_val = st.text_input("Valor mínimo:", value="1")
max_val = st.text_input("Valor máximo:", value="18")

# Verifica se os valores são válidos
if min_val.isdigit() and max_val.isdigit():
    min_val = int(min_val)
    max_val = int(max_val)

    if min_val < max_val:
        if st.button('Gerar Número'):
            number = random.randint(min_val, max_val)
            st.markdown(f"<div class='center-number'>{number}</div>", unsafe_allow_html=True)
    else:
        st.error("O valor mínimo deve ser menor que o valor máximo.")
else:
    st.error("Por favor, insira números inteiros válidos.")
