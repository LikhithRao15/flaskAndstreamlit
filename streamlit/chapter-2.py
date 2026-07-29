# pyrefly: ignore [missing-import]
import streamlit as st
from datetime import datetime,date

 
st.title("Simple app")
if st.button("Click me"):
    st.success("you clicked the button successfully")


message=st.checkbox("show message")

if message:
    st.write("the message is visible now")

selected= st.radio("select the option",["option1","option2","option3"])

if selected:
    st.write("you selected ",selected)

value=st.slider("select a value",0,100,25)

st.write("you selected ",value)


st.number_input("enter your age",min_value=18,max_value=120,step=1)

name=st.text_input("Enter your name")
if name:
    st.write(f"hello {name}")
    
today=st.date_input("today's date",datetime.now())

dob=st.date_input("Enter your date of birth",min_value=date(2000,1,1))

age = today.year - dob.year 
st.write(f"your age is {age}")