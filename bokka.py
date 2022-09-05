import streamlit as st 
st.header('RCEEEEEE')
a=st.number_input('Enter any value')
if st.button('okay'):
  st.success(f'ur lucky number is{a}')
