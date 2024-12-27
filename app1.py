# streamlit 라이브러리 불러오기
import streamlit as st
import json
import os
import random
import string

# 데이터 저장 파일 경로
DATA_FILE = "shared_data.json"
USER_DATA_FILE = "users_data.json"


# 데이터 초기화 또는 로드
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({ "c": [[[None for _ in range(50)] for _ in range(15)] for _ in range(8)]}, f)

if not os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, "w") as f:
        json.dump({ "b": [[0]for _ in range(8)], "d" : [None]}, f)


# 데이터 로드 함수
def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# 데이터 저장 함수
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_user_data_id():
    if not os.path.exists(USER_DATA_FILE):
        return []  # 파일이 없으면 빈 리스트 반환
    
    try:
        with open(USER_DATA_FILE, "r") as f:
            data = json.load(f)
            return data.get("d", []) if isinstance(data, dict) else []
    except json.JSONDecodeError:
        print(f"ERROR: {USER_DATA_FILE} 파일의 JSON 형식이 잘못되었습니다.")
        return []
    except Exception as e:
        print(f"ERROR: {USER_DATA_FILE} 파일 읽는 중 오류 발생: {e}")
        return []

def load_user_data_class():
    if not os.path.exists(USER_DATA_FILE):
        return [[] for _ in range(8)]  # 파일이 없으면 기본값 반환
    
    try:
        with open(USER_DATA_FILE, "r") as f:
            data = json.load(f)
            return data.get("b", [[] for _ in range(8)]) if isinstance(data, dict) else [[] for _ in range(8)]
    except json.JSONDecodeError:
        print(f"ERROR: {USER_DATA_FILE} 파일의 JSON 형식이 잘못되었습니다.")
        return [[] for _ in range(8)]
    except Exception as e:
        print(f"ERROR: {USER_DATA_FILE} 파일 읽는 중 오류 발생: {e}")
        return [[] for _ in range(8)]


# 사용자 데이터 저장 함수
def save_user_data_id(users_d):
    try:
        # 기존 데이터 로드
        if os.path.exists(USER_DATA_FILE):
            with open(USER_DATA_FILE, "r") as f:
                data = json.load(f)
        else:
            data = {}

        # "d" 데이터 업데이트
        data["d"] = users_d

        # JSON 파일에 저장
        with open(USER_DATA_FILE, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"ERROR: 사용자 데이터를 저장하는 중 오류 발생: {e}")

def save_user_data_class(users_b):
    try:
        # 기존 데이터 로드
        if os.path.exists(USER_DATA_FILE):
            with open(USER_DATA_FILE, "r") as f:
                data = json.load(f)
        else:
            data = {}

        # "b" 데이터 업데이트
        data["b"] = users_b

        # JSON 파일에 저장
        with open(USER_DATA_FILE, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"ERROR: 사용자 데이터를 저장하는 중 오류 발생: {e}")


# 데이터 로드
data = load_data()
c = data["c"]

# 로그인 함수
def login():
    if "user_id" not in st.session_state:  # 세션에 사용자 ID가 없으면 로그인 화면을 표시
        st.session_state.user_id = None  # 사용자 ID 초기화
        st.session_state.logged_in = False  # 로그인 여부 초기화
        return False
    
    if st.session_state.logged_in:  # 로그인되어 있다면, 사용자 ID 표시
        st.write(f"로그인 성공! 사용자 ID: {st.session_state.user_id}")
        return True
    else:
        return False

# 랜덤 ID 생성 함수
def generate_random_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=4))

# 로그인 화면 표시
def show_login_form(users):
    st.subheader("로그인 / 아이디 생성")

    user_id_input = st.text_input("아이디를 입력하세요.", key="login_id")

    st.write("\n\n 새 아이디를 만들 분은 고유 아이디를 입력해주세요.")
    user_id_text = st.text_input("고유 아이디를 입력하세요.")
    # 새 아이디 생성 버튼 클릭 시 랜덤 아이디 생성
        
    create_id_button = st.button("새 아이디 만들기")
    if create_id_button:
        if user_id_text:
            user_id_general = generate_random_id()
            user_id_input = user_id_general + user_id_text
            users.append(user_id_input)
            save_user_data_id(users) 
            st.session_state.user_id = user_id_input
            st.write(f"생성된 아이디: {user_id_input}")
            st.session_state.logged_in = True
        

    # 로그인 버튼 클릭 시
    if st.button("로그인"):
        if user_id_input in users:
            st.session_state.user_id = user_id_input
            st.session_state.logged_in = True  # 로그인 상태 변경
        else:
            st.warning("잘못된 아이디입니다. 다시 시도하세요.")

# 세션에 로그인 여부 확인
if not login():
    users = load_user_data_id()  # 저장된 사용자 목록을 불러옴
    show_login_form(users)  # 로그인 화면을 띄움
else :
    
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
          st.write('- 나만의 반 만들기(최대 8개) : 모든 학생의 학번 입력 후 반생성 다시 클릭')
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
                      
    if (a == '나만의 반 만들기'):
        n = st.number_input('반 총 인원수를 입력해주세요.', value=0, step=1)
        b = load_user_data_class()
        if st.button('반 생성'):
            if (len([x for x in b if x]) >= 8):
                st.warning("반을 생성할 수 없습니다. (8개 모두 만들었습니다.)")
            else:
                input_data = st.text_area('학번들을 입력해주세요 (쉼표로 구분)', "")
                if input_data:
                    n_li = [int(x.strip()) for x in input_data.split(',')]  # 쉼표로 구분된 학번을 리스트로 변환
                    if len(n_li) == n:  # 입력된 학번 수가 반 인원 수와 일치하면 반을 생성
                        for idx in range(len([x for x in b if x])):
                            if not b[idx]:
                                b[idx] = n_li
                                break
                        save_user_data_class(b) 
                        output_containers[len([x for x in b if x]) - 1].write(f"{len([x for x in b if x]) - 1}번 반 생성 완료. 학생 명단: {n_li}")
                    else:
                        st.warning(f"입력된 학번 수가 반 인원수와 일치하지 않습니다. {n}명의 학번을 입력해주세요.")
              
    if a == '나만의 반 확인':
        n = st.number_input('반의 코드를 적으세요.', value=0, step=1)
        if st.button('확인'):
            b = load_user_data_class()
            if  n < 0 or n >=len([x for x in b if x]) or not b[n]:
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
            b = load_user_data_cㅣass()
            if n < 0 or n >= len([x for x in st.session_state.b if x]) or not b[n]:
                st.warning("해당 반 정보가 없거나 이미 삭제되었습니다.")
            else:
                deleted_class = b[n]
                b[n] = []
                save_user_data_class(b) 
                output_containers[n].empty()
                st.success(f"{n}번 반이 삭제되었습니다. 삭제된 학생 명단: {deleted_class}")
