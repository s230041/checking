# streamlit 라이브러리 불러오기
import streamlit as st      
b = [0]*40000
c = [[None for i in range(50)]for i in range(11)]
alpha = 0
beta = 0
# 제목 쓰기
st.title('학생 체킹')   

# 여러 개의 열(문단)을 생성
col1, col2 = st.columns(2)       
# 왼쪽 문단
with col1:
      st.subheader('*사용방법*')
      st.write('- 확인 : 출석체크 확인 (학번 입력)')
      st.write('- 체크 : 출석체크 (학번 상태 입력 ex : 2110801)')
      st.write('- 반 전체 확인 : 11반중 선택')
      st.write('- 나만의 반 만들기 : 모든 학생의 학번 입력')

a = st.selectbox('사용할 기능을 고르세요!', ['확인','체크','반 전체 확인', '나만의 반 만들기'])
if (a == '확인'):
      n= st.number_input('수를 입력하세요', value = 0)
      
