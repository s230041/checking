# streamlit 라이브러리 불러오기
import streamlit as st      
b = [{},{},{},{},{},{},{}]
c = [[[" " for j in range(50)]for i in range(15)]for k in range(8)]
count = 0
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
      st.write('- 나만의 반 확인')

a = st.selectbox('사용할 기능을 고르세요!', ['확인','체크','반 전체 확인', '나만의 반 만들기'])
if (a == '확인'):
      n = st.number_input('학번을 입력해주세요.',value = 0)
      w = c[n//10000][(n//100)%100][n%10]
      st.success(w)
elif (a == '체크'):
      n = st.number_input('학번을 입력해주세요.', value = 0)
      w = st.text_input('상태를 입력해주세요.')
      if st.button('체킹'): 
            c[n//10000][(n//100)%100][n%10] = w
            st.success(w)

elif (a == '반 전체 확인'):
      n1 = st.number_input('학년을 입력해주세요.',value = 0)
      n2 = st.number_input('반을 입력해주세요.', value = 0)
      for i in c[n1][n2]:
            if(i != 0):
                  st.write(i)
                  
elif (a == '나만의 반 만들기'):
      n = st.number_input('반 총 인원수를 입력해주세요.', value = 0)
      for i in range(n):
            n1 = st.number_input('학번을 입력해주세요.', value = 0)
            b[count].append(n1)
      count+=1
      with col2:
            st.write('총 인원수',n,count-1,'반\n', b[count-1])
elif(a == '나만의 반 확인'):
      n = st.number_input('반의 코드를 적으세요.',value = 0)
      for i in b[n]:
            st.write(i, c[i//10000][(i//100)%100][i%10])
            
      


