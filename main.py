import streamlit as st
st.title('대구고등학교 홈페이지')


st.header('학교소개')
st.header('교육활동')
st.caption('학급마당')

sample_code = '''
def function():
    print('hello, world')
'''
st.code(sample_code, language="python")

st.text("기본 텍스트")
st.markdown('streamlit은 **마크다운 문법을 지원**합니다.')
# markdown() : 서식이 있는 문자 사용시
# **~**: 볼드체 표시
# :(색상)[입력할 글자] -> 색상 변경
# 예: :red[?] -> 빨간색 글자 표시
st.markdown('**:blue[최예나]**')
st.markdown("텍스트의 색상을 :green[초록색]으로, 그리고 **:blue[파란색]** 볼드체로 설정할 수 있습니다.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$]와 같이 latex 문법의 수식 표현도 가능합니다. :pencil:")