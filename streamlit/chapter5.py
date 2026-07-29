import streamlit as st 
import requests

st.title("Live curency converter")

currency=st.number_input("Enter amount",min_value=1)
convert=st.selectbox("convert to",["USD","JPY","EUR","GBP"])

if st.button("convert"):
    url="https://v6.exchangerate-api.com/v6/8cea9462d14a682b147281be/latest/INR"
    response=requests.get(url)

    if response.status_code==200:
        data=response.json()
        rate=data["conversion_rates"][convert]
        converted=rate*currency
        st.success(f"{currency} INR = {converted} {convert}")
    else:
        st.error("could not fetch latest exchange rate")
    