# streamlit 라이브러리 불러오기
import streamlit as st
import json
import os

# 데이터 저장 파일 경로
DATA_FILE = "shared_data.json"

# 데이터 초기화 또는 로드
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({ "c": [[[None for _ in range(50)] for _ in range(15)] for _ in range(8)]}, f)
        
if 'b' not in st.session_state:
    st.session_state.b = [[] for _ in range(8)]

# 데이터 로드 함수
def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# 데이터 저장 함수
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# 데이터 로드
data = load_data()
b = st.session_state.b
c = data["c"]

output_containers = [st.empty() for _ in range(8)]

# 제목 쓰기
st.title('학생 체킹')   

# 여러 개의 열(문단)을 생성
col1, col2 = st.columns(2)       
# 왼쪽 문단
with col1:
      st.subheader('*사용방법*')
      st.write('- 확인 : 출석체크 확인 (학번 입력)')
      st.write('- 체크 : 출석체크 (학번 상태 입력 ex : 21108)')
      st.write('- 반 전체 확인 : 11반중 선택')
      st.write('- 나만의 반 만들기(최대 8개) : 모든 학생의 학번 입력')
      st.write('- 나만의 반 확인 : 반 상태 확인')
      st.write("- 나만의 반 삭제 : 반을 제거하세요.")
a = st.selectbox('작업할 기능을 고르세요',['확인','체크','반 전체 확인','나만의 반 만들기','나만의 반 확인','나만의 반 삭제'])
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
            data["c"] = c
            save_data(data)
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
        if len(b) >= 8:
            st.warning("반을 생성할 수 없습니다. (8개 모두 만들었습니다.)")
        else:
            n_li = []
            for i in range(n):
                nn = st.number_input(f'{i + 1}번 학번 입력:', value=0, step=1, key=f"student_{i}")
                n_li.append(nn)
            b[len(b)] = (n_li)
            output_containers[len(b) - 1].write(f"{len(b) - 1}번 반 생성 완료. 학생 명단: {n_li}")

          
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

if a == '나만의 반 삭제':
    n = st.number_input('삭제할 반의 코드를 입력하세요.', value=0, step=1)
    if st.button('삭제'):
        if n < 0 or n >= len(b) or not b[n]:
            st.warning("해당 반 정보가 없거나 이미 삭제되었습니다.")
        else:
            deleted_class = b[n]
            b[n] = []
            output_containers[n].empty()
            st.success(f"{n}번 반이 삭제되었습니다. 삭제된 학생 명단: {deleted_class}")
