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

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="ATENTOS Novus Hotel", page_icon="🛏️")
st.title('ATENTOS 🛏️ Novus Hotel')
st.subheader(':blue[New Sales, Confirmation, Welcoming & Support Clients]👤')
current_time = time.ctime()
st.write("In real time monitoring at: ", current_time)

st.write('---')

st.header('🤖🤵🏻Virtual Butlers🤵🏻‍♂️🤖')
colored_header(
    label="Funnels by cycles",
    description="Plans, Tasks & Results",
    color_name="violet-70",
)
topic = st.selectbox("Choose the Stage of UX of 👤Clients👥 & 🤖Butlers🎩:",
        ("New Sales", "Confirmations", "Welcomings", "Support"),
    )
