import streamlit as st

st.title("hello world")
st.subheader("by Likhith Rao O")
st.text("welcome to my stream")
st.write("## this is a markdown text")



programming_language=st.selectbox("programming languages",["python","java","C","C++"])

st.write("you selected ",programming_language)

st.success("success message")
 