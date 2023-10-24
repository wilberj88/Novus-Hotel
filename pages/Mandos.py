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
col1, col2, col3 = st.columns(3)
with col1:
  acelerometro1 = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                    },
                },
                "progress": {"show": "true", "width": 10},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": 85, "name": "Reservations"}],
            }
        ],
    }

  st_echarts(options=acelerometro1)

with col2:
  acelerometro2 = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                    },
                },
                "progress": {"show": "true", "width": 10},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": 70, "name": "Ocupation"}],
            }
        ],
    }

  st_echarts(options=acelerometro2)

with col3:
  acelerometro3 = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                    },
                },
                "progress": {"show": "true", "width": 10},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": 100, "name": "Cleaning"}],
            }
        ],
    }
  st_echarts(options=acelerometro3)

colored_header(
    label="Alarms",
    description="Temporal, Climatological & Inflation warnings of danger",
    color_name="red-70",
)

#ALARMS CONFIGURATION
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "146090ad17fa8843bc9eca97c53926b4"
sity1 = "New York"
sity2 = "Colchester"
URL1 = BASE_URL + "q=" + sity1 + "&appid=" + API_KEY
URL2 = BASE_URL + "q=" + sity2 + "&appid=" + API_KEY
response1 = requests.get(URL1)
response2 = requests.get(URL2)

if response1.status_code == 200:
   # getting data in the json format
   data1 = response1.json()
   # getting the main dict block
   main1 = data1['main']
  # getting temperature
   temperature1 = main1['temp']
   # getting the humidity
   humidity1 = main1['humidity']
   # getting the pressure
   pressure1 = main1['pressure']
   # weather report
   report1 = data1['weather']

if response2.status_code == 200:
   # getting data in the json format
   data2 = response2.json()
   # getting the main dict block
   main2 = data2['main']
  # getting temperature
   temperature2 = main2['temp']
   # getting the humidity
   humidity2 = main2['humidity']
   # getting the pressure
   pressure2 = main2['pressure']
   # weather report
   report2 = data2['weather']

pytrends = TrendReq(hl='en-US', tz=360)
col4, col5, col6 = st.columns(3)

with col4:
    st.write("🇺🇸 Top10 Trending Search in last hour")
    # Google Trends data
    df1 = pytrends.trending_searches(pn='united_states')
    st.dataframe(df1.head(10))

with col5:
    st.write(f"{sity1:-^30}")
    st.write(f"Temperature (Kelvins): {temperature1}")
    st.write(f"Humidity: {humidity1}")
    st.write(f"Pressure: {pressure1}")
    st.write(f"Weather Report: {report1[0]['description']}")
    st.write(f"{sity2:-^30}")
    st.write(f"Temperature (Kelvins): {temperature2}")
    st.write(f"Humidity: {humidity2}")
    st.write(f"Pressure: {pressure2}")
    st.write(f"Weather Report: {report2[0]['description']}")
    
with col6:
     col6.metric("Sentimiento", "86%", "4%")

colored_header(
    label="Recommendations",
    description="Temporal, Climatological & Inflation suggestions",
    color_name="blue-70",
)


st.write('---')
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


st.write('---')
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


st.write('---')
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


st.write('---')
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

st.write('---')
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

st.write('---')
st.header('Rentability')
