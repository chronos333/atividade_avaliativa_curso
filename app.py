import streamlit as st
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage


st.set_page_config(page_title="Chatbot NXR", layout="wide")
st.title(" Suporte Técnico - Nobreak NXR 15-90kVA")

API_KEY = st.secrets.get("OPENAI_API_KEY")

if not API_KEY:
    st.error("Configure sua OPENAI_API_KEY no st.secrets")
    st.stop()

OBJETOS_AUTORIZADOS = ["1234", "5678", "9999"]

if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if "led" not in st.session_state:
    st.session_state.led = False

if not st.session_state.autenticado:
    st.subheader("Acesso restrito")

    codigo = st.text_input("Digite seu código de acesso:", type="password")

    if st.button("Entrar"):
        if codigo in OBJETOS_AUTORIZADOS:
            st.session_state.autenticado = True
            st.session_state.led = True
            st.success("Acesso autorizado ")
        else:
            st.error("Acesso negado ")

    st.stop()


if st.session_state.led:
    st.success("LED LIGADO (Usuário autorizado)")


@st.cache_data
def carregar_dados():
    return pd.read_csv("alarmes.csv")

df = carregar_dados()


def buscar_contexto(pergunta):
    pergunta = pergunta.lower()

    resultados = df[
        df["Alarme"].str.lower().str.contains(pergunta) |
        df["Descricao"].str.lower().str.contains(pergunta)
    ]

    if resultados.empty:
        return None

    contexto = ""
    for _, row in resultados.iterrows():
        contexto += f"""
Alarme: {row['Alarme']}
Descrição: {row['Descricao']}
Solução: {row['Solucao']}
"""

    return contexto


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
    openai_api_key=API_KEY
)

def gerar_resposta(pergunta, contexto):
    prompt = f"""
Você é um especialista em Nobreak NXR 15-90kVA.

Responda de forma objetiva e profissional com base SOMENTE nos dados abaixo:

{contexto}

Pergunta: {pergunta}

Regras:
- Máximo 10 linhas
- Seja direto
- Se não souber:
"Informação não encontrada no manual. Contate o suporte."
"""

    resposta = llm([HumanMessage(content=prompt)])
    return resposta.content


if "messages" not in st.session_state:
    st.session_state.messages = []

st.subheader("Chat Técnico")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

pergunta = st.chat_input("Descreva o problema do nobreak...")

if pergunta:
    st.session_state.messages.append({"role": "user", "content": pergunta})

    with st.chat_message("user"):
        st.write(pergunta)

    contexto = buscar_contexto(pergunta)

    if contexto:
        resposta = gerar_resposta(pergunta, contexto)
    else:
        resposta = "Informação não encontrada no manual. Contate o suporte."

    st.session_state.messages.append({"role": "assistant", "content": resposta})

    with st.chat_message("assistant"):
        st.write(resposta)


if len(st.session_state.messages) > 20:
    st.session_state.messages = st.session_state.messages[-20:]