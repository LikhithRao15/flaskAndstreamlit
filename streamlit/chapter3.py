# pyrefly: ignore [missing-import]
import streamlit as st

st.title("Poll")

col1,col2=st.columns(2)

with col1:
    st.header("Column 1")
    vote1=st.button("Vote for option1")
with col2:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7qftW1PRWr5Q7gWVXrcodDKblW19CwZHvSXVw74M5Ww&s=10",width=300)
    vote2=st.button("Vote for option2")

if vote1:
    st.success("you voted for option 1")
    
if vote2:
    st.success("you voted for option 2")


name=st.sidebar.text_input("enter your name")

with st.expander("about me"):
    st.write(f"hello welcome to this app") 

st.markdown('##hello world')