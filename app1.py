# streamlit 라이브러리 불러오기
import streamlit as st      
if 'b' not in st.session_state:
    st.session_state.b = [[] for _ in range(8)]  # "나만의 반" 저장 리스트
if 'c' not in st.session_state:
    st.session_state.c = [[[None for _ in range(50)] for _ in range(15)] for _ in range(8)]
if 'count' not in st.session_state:
    st.session_state.count = 0


b = st.session_state.b
c = st.session_state.c
count = st.session_state.count

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
a = st.selectbox('작업할 기능을 고르세요',['확인','체크','반 전체 확인','나만의 반 만들기','나만의 반 확인'])
if (a == '확인'):
      n = st.number_input('학번을 입력해주세요.',value = 0)
      if st.button('확인'):
            n1 = n//10000
            n2 = (n//100)%100
            n3 = n%100
            st.success(c[n1][n2][n3])
if (a == '체크'):
      n = st.number_input('학번을 입력해주세요.', value = 0)
      w = st.text_input('상태를 입력해주세요.')
      if st.button('체킹'):
            n1 = n//10000
            n2 = (n//100)%100
            n3 = n%100
            c[n1][n2][n3] = w
            st.success(f"{n}번 상태 저장: {w}")

if (a == '반 전체 확인'):
      n1 = st.number_input('학년을 입력해주세요.',value = 0)
      n2 = st.number_input('반을 입력해주세요.', value = 0)
      if st.button('확인'):
            st.write(f"학년 {n1}, 반 {n2} 출석 상태:")
            for i,j in enumerate(c[n1][n2]):
                  st.write(f"{i}번 : {j}")
                  
if a == '나만의 반 만들기':
    n = st.number_input('반 총 인원수를 입력해주세요.', value=0, step=1)
    if st.button('반 생성'):
        n_li = []
        for i in range(n):
            n = st.number_input(f'{i + 1}번 학번 입력:', value=0, step=1, key=f"student_{i}")
            n_li.append(n)
        b[count] = n_li
        st.session_state.count += 1
        st.write(f"{count}번 반 생성 완료. 학생 명단: {n_li}")
          
if a == '나만의 반 확인':
    n = st.number_input('반의 코드를 적으세요.', value=0, step=1)
    if st.button('확인'):
        if n >= len(b) or not b[n]:
            st.warning("해당 반 정보가 없습니다.")
        else:
            st.write(f"{n}번 반 학생 상태:")
            for nn in b[n]:
                n1 = nn // 10000
                n2 = (nn // 100) % 100
                n3 = nn % 100
                n4 = c[n1][n2][n3]
                st.write(f"{nn}: {n4 if n4 else '상태 없음'}")


