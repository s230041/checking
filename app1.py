# streamlit 라이브러리 불러오기
import streamlit as st      
b = [0 for i in range(40000)]
c = [[0 for i in range(50)]for i in range(11)]
# 제목 쓰기
st.title('동생아 _________')  
# 부제목 쓰기
st.subheader('오늘의 주제: _______')
# 본문 쓰기
st.write('음수?? ______않아!') 

# 여러 개의 열(문단)을 생성
col1, col2 = st.columns(2)       
# 왼쪽 문단
with col1:
      st.subheader('*사용방법*')
      st.write('- 확인 : 출석체크 확인 (학번 입력)')
      st.write('- 체크 : 출석체크 (학번 상태 입력 ex : 21108 출석)')
      st.write('- 반 전체 확인 : 11반중 선택')
      st.write('- 나만의 반 만들기 : 모든 학생의 학번 입력')


# 사용자의 입력을 받아서 a에 저장하기(초기값은 0)
#a = st.number_input('____________', value= ____)  

# 버튼 생성 및 동작
if st.button('체크'):
  a= st.input()
  for i in range(len(a)):
    if(a[i] == ' '):
      b[int(a[:i:])] = a[i::]
      break
      

if st.button('확인'):
  a= st.input()
  if b[a] != 0 :
    print(b[a])
