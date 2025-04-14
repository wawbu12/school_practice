import matplotlib
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc, font_manager
import seaborn as sns
import numpy as np

data = pd.DataFrame({
    '이름': ['영식', '철수', '영희'],
    '나이': [22, 31, 25],
    '몸무게': [75.5, 80.2, 55.1]
})

st.dataframe(data, use_container_width=True)

font_path = "C:\WINDOWS\Fonts\GULIM.TTC"
font = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font)

fig, ax = plt.subplots()
ax.bar(data['이름'], data['나이'])
st.pyplot(fig)

# fig 그래프 그림
# ax : 객체는 그래프를 그릴 영역 선택
fig1, ax = plt.subplots()
plt.title("개인별 나이")
ax.bar(data['이름'], data['나이'])
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.1f'),
                # 텍스트를 표시할 위치를 지정, 중간위치ㅡ 높이값 지정
                (p.get_x() + p.get_width() / 2., p.get_height()),
                # 텍스트의 가로위치(ha)와 세로위치(va)를 'center'로
                # 설정하여 텍스트가 가운데 정렬되도록 지정
                ha='center', va='center',
                # 텍스트를 막대 위, 9 픽셀 위에 표시
                xytext=(0, 9),
                textcoords="offset points")
ax.set_ylim(0, 40)
st.pyplot(fig1)

path = '인구.csv'
data1 = pd.read_csv(path, encoding='cp949')
print(data1)
st.dataframe(data1, use_container_width=True)

fig3, ax = plt.subplots()
plt.title("개인별 나이")
ax.bar(data1['시점'], data1['출생아수(명)'])
plt.xlabel("연도")
plt.ylabel("출생아수(단위: 명)")
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.1f'),
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center',
                xytext=(0, 9),
                textcoords="offset points")
ax.set_ylim(200000, 500000)
st.pyplot(fig3)

fig4, ax = plt.subplots()
plt.title("연도별 출생아수(선형)")
ax.plot(data1['시점'], data1['출생아수(명)'], color="#58D3F7", marker=",", linestyle="-")
plt.xlabel("연도")
plt.ylabel("출생아수(단위: 명)")
for i, txt in enumerate(data1['출생아수(명)']):
    ax.text(data1['시점'][i], txt, str(txt), ha='center', va='bottom')
ax.set_ylim(200000, 500000)
st.pyplot(fig4)

plt.plot([1, 2, 3], marker=11)
plt.plot([1, 2, 3], marker=matplotlib.markers.CARETDOWNBASE)

linestyle_str = [
     ('solid', 'solid'),      # Same as (0, ()) or '-'
     ('dotted', 'dotted'),    # Same as (0, (1, 1)) or ':'
     ('dashed', 'dashed'),    # Same as '--'
     ('dashdot', 'dashdot')]  # Same as '-.'
