import streamlit as st
from streamlit_card import card
from streamlit_extras.grid import grid
from streamlit_extras.colored_header import colored_header
import folium
from streamlit_folium import st_folium
import time
from streamlit_echarts import st_echarts
import pytrends
from pytrends.request import TrendReq
import requests
import random

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="ATENTOS Novus Hotel", page_icon="🛏️")
st.title('ATENTOS 🛏️ Novus Hotel')

current_time = time.ctime()
st.write("In real time operation at: ", current_time)

if "messages" not in st.session_state:
st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
with st.chat_message(message["user"]):
    st.markdown(message["👋Bienvenido a Novus legal ⚖️: pregúntame lo que quieras sobre tu caso"])
# React to user input
if prompt := st.chat_input("Dímelo de una"):
# Display user message in chat message container
st.chat_message("user").markdown(prompt)
# Add user message to chat history
st.session_state.messages.append({"role": "user", "content": prompt})

response = f"Echo: {prompt}"
# Display assistant response in chat message container
with st.chat_message("assistant"):
    message_placeholder = st.empty()
    full_response = ""
    assistant_response = random.choice(
        [
            "Su consulta está ahora en las mejores manos, en breve enviamos reporte de consulta jurídica",
            "Claro que sí, cuente con mi apoyo jurídico en todo su proceso judicial",
            "Por supuesto que sí, estoy para defender todos tus derechos, cuentas conmigo",
        ]
    )
    # Simulate stream of response with milliseconds delay
    for chunk in assistant_response.split():
        full_response += chunk + " "
        time.sleep(0.1)
        # Add a blinking cursor to simulate typing
        message_placeholder.markdown(full_response + "▌")
    message_placeholder.markdown(full_response)
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": full_response})
        
st.write('---')

stage = st.selectbox("Choose the Stage of UX of 👤Clients👥 & 🤖Butlers🎩:",
        ("New Sales", "Confirmations", "Welcomings", "Support"),
    )



st.subheader(':blue[New Sales, Confirmation, Welcoming & Support Clients]👤')

st.header('🤖🤵🏻Virtual Butlers🤵🏻‍♂️🤖')
colored_header(
    label="Texts, Audios & Funnels by cycles",
    description="Plans, Tasks & Results",
    color_name="violet-70",
)
