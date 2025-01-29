# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1rX1gBG4FA4-BG6_JM0yHY_JqrYBHqOjn59RFIQgDZhI/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

#data = conn.read(spreadsheet=url, usecols=[0, 1, 2, ])
#st.dataframe(data)
st.header("Realisasi Anggaran Pembangunan Gereja")
st.subheader("Gereja Katolik Roh Kudus Kebonarum")
st.write("Dion Dharmawan")
st.image(gereja.jpg)

sql = '''
SELECT
    "LINGKUNGAN"

FROM
    "kimak"
'''
data = conn.read(spreadsheet=url, worksheet="1972598785", ttl=1 ) # Define Worksheet
st.dataframe(data)

df_infentory_health = conn.query(spreadsheet=url, sql=sql)
st.dataframe(df_infentory_health)