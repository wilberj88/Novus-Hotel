import streamlit as st
from streamlit_card import card
from streamlit_extras.grid import grid
from streamlit_extras.colored_header import colored_header
import folium
from streamlit_folium import st_folium
import time


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="MANDOS Novus Hotel", page_icon="🛏️")

st.title('MANDOS 🛏️ Novus Hotel')
current_time = time.ctime()
st.write("In real time monitoring at: ", current_time)


st.header('Suits')
colored_header(
    label="Operation",
    description="Reservations, Ocupation & Cleaning",
    color_name="violet-70",
)

colored_header(
    label="Alarms",
    description="Temporal, Climatological & Inflation warnings of danger",
    color_name="red-70",
)

colored_header(
    label="Recommendations",
    description="Temporal, Climatological & Inflation suggestions",
    color_name="blue-70",
)

st.header('Rooms')
colored_header(
    label="Operation",
    description="Reservations, Ocupation & Cleaning",
    color_name="violet-70",
)

colored_header(
    label="Alarms",
    description="Temporal, Climatological & Inflation warnings of danger",
    color_name="red-70",
)

colored_header(
    label="Recommendations",
    description="Temporal, Climatological & Inflation suggestions",
    color_name="blue-70",
)


st.header('Beds')
colored_header(
    label="Operation",
    description="Reservations, Ocupation & Cleaning",
    color_name="violet-70",
)

colored_header(
    label="Alarms",
    description="Temporal, Climatological & Inflation warnings of danger",
    color_name="red-70",
)

colored_header(
    label="Recommendations",
    description="Temporal, Climatological & Inflation suggestions",
    color_name="blue-70",
)
st.header('Staff')
colored_header(
    label="Operation",
    description="Working, Resting & Payments",
    color_name="violet-70",
)

colored_header(
    label="Alarms",
    description="Temporal, Climatological & Talent Market`s warnings of danger",
    color_name="red-70",
)

colored_header(
    label="Recommendations",
    description="Temporal, Climatological & Business suggestions",
    color_name="blue-70",
)
st.header('Expenditures')
colored_header(
    label="Operation",
    description="Reservations, Ocupation & Cleaning",
    color_name="violet-70",
)

colored_header(
    label="Alarms",
    description="Temporal, Climatological & Inflation warnings of danger",
    color_name="red-70",
)

colored_header(
    label="Recommendations",
    description="Temporal, Climatological & Inflation suggestions",
    color_name="blue-70",
)


st.header('Savings')
colored_header(
    label="Operation",
    description="Reservations, Ocupation & Cleaning",
    color_name="violet-70",
)

colored_header(
    label="Alarms",
    description="Temporal, Climatological & Inflation warnings of danger",
    color_name="red-70",
)

colored_header(
    label="Recommendations",
    description="Temporal, Climatological & Inflation suggestions",
    color_name="blue-70",
)
