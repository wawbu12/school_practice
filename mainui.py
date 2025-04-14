import streamlit as st
import pandas as pd

# ---------------------------------
st.title('<:red[성적]확인하기>')

button = st.button('보내기')
if button:
    st.write(':blue[메세지]를 보냈습니다')

data = pd.DataFrame({
    'number': [10101, 10102, 10103, 10104],
    'name': ['kim', 'lee', 'choi', 'park'],
    'score': [85, 95, 100, 70]
})
# ----------------------------------

# 다운로드 버튼을 생성하고 데이터와 연결
st.download_button(
    label='성적 다운로드',
    data=data.to_csv(),
    file_name='sample.csv',
    mime='text/csv'
)

agree = st.checkbox('개인정보수집 동의하십니까?')
if agree:
    st.write('동의해주셔서 감사합니다 :100:')
else:
    st.write('동의하지 않으시면 서비스 이용에 제한이 생길 수 있습니다.')

mbti = st.radio(
    '당신의 MBTI는 무엇입니까?',
    ('object', 'ISTJ', 'ENFP', 'INTP', '선택지 없음'))
if mbti == 'object':
    st.write('**아래 버튼**을 클릭해주세요.')
elif mbti == 'ISTJ':
    st.write('당신은 :blue[현실주의자] 이시네요')
elif mbti == 'ENFP':
    st.write('당신은 :green[활동가] 이시네요')
elif mbti == 'INTP':
    st.write('당신은 :red[사색가] 이시네요')
else:
    st.write("당신에 대해 :red[알고 싶어요]:grey_exclamation")

mbti = st.selectbox(
    '당신의 MBTI는 무엇입니까?',
    ('object', 'ISTJ', 'ENFP', 'INTP', '선택지 없음'),
    index=0
)
if mbti == 'object':
    st.write('**아래 버튼**을 클릭해주세요.')
elif mbti == 'ISTJ':
    st.write('당신은 :blue[현실주의자] 이시네요')
elif mbti == 'ENFP':
    st.write('당신은 :green[활동가] 이시네요')
elif mbti == 'INTP':
    st.write('당신은 :red[사색가] 이시네요')
else:
    st.write("당신에 대해 :red[알고 싶어요]:grey_exclamation:")

options = st.multiselect(
    '당신이 좋아하는 과일은 뭔가요?',
    ['망고', '오렌지', '사과', '바나나'],
    ['망고', '오렌지'])
st.write(f'당신의 선택은: :red[{options}]입니다.')

values = st.slider(
    '키:sparkles:',
    140.0, 190.0, (165.0, 175.0))
st.write('선택범위:', values)

name = st.text_input(
    label='이름을 입력하세요',
    placeholder='ex) 홍길동'
)

song = st.text_input(
    label='**:blue[Newjeans]** 가사 모음',
    placeholder='예시: "attention"을 입력해보세요!'
)

title = st.text_input(
    label='가고 싶은 여행지가 있나요?',
    placeholder='여행지를 입력해주세요'
)
st.write(f'{name}님이 선택한 여행지: :violet[{title}]')

number = st.number_input(
    label='나이를 입력해주세요',
    min_value=10,
    max_value=100,
    value=30,  # 초기값
    step=5  # 5씩 증가 !!
)
st.write('당신의 나이는: ', number)
