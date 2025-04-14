import streamlit as st
st.title("새 탭 만들기!")

image_path = '해린.png'
st.image(image_path)

name = st.radio('누구게요~', ['강해린', '고양이', '한결'])
if name == '강해린':
    st.write('정답!')
elif name == '고양이':
    st.write('비슷한데 정답은 아님')
elif name == '한결':
    st.write('**넌 나가라**')