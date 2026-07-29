import streamlit as st
import pandas as pd

st.title("data analysis ")

file=st.file_uploader("upload your dataset",type=["csv"])

if file:
    df=pd.read_csv(file)
    st.subheader("dataset")
    st.dataframe(df)

if file:
    cities=df["City"].unique()
    selected_city=st.selectbox("Select a city",cities)
    df_filtered=df[df["City"]==selected_city]
    st.dataframe(df_filtered)
   
    