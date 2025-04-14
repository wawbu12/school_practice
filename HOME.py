import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc, font_manager

st.title(':blue[New Jeans]')
st.caption("**버니즈 클럽**")

st.subheader('뉴진스를 소개합니다')
button = st.button('강해린')
if button:
    image_path = '해린.png'
    st.image(image_path)
    st.write('이름 : **강해린**')
    st.write('출생 : **2006.05.15**')
button1 = st.button('팜하니')
if button1:
    image_path = '하니.png'
    st.image(image_path)
    st.write('이름 : **하니 팜**')
    st.write('출생 : **2004.10.06**')
button2 = st.button('다니엘')
if button2:
    image_path = '다니.png'
    st.image(image_path)
    st.write('이름 : **모지혜**')
    st.write('출생 : **2005.04.15**')
button3 = st.button('혜인')
if button3:
    image_path = '혜인.png'
    st.image(image_path)
    st.write('이름 : **이혜인**')
    st.write('출생 : **2008.04.21**')