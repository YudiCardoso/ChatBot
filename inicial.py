import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key="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")

st.write("# Chat bot com IA")

if not("lista_mensagens") in st.session_state:
    st.session_state["lista_mensagens"] = []

texto_usuario = st.chat_input("Digite sua mensagem")

# exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

#Pergunta do usuario
if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {"role":"user", "content":texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)

#Resposta IA
    resposta_modelo = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    )
    resposta_ia = resposta_modelo.choices[0].message.content
    
    # exibir a resposta da IA na tela
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role":"assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
