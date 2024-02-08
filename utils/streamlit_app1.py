import streamlit as st

st.set_page_config(
    page_title="신원 확인",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="auto"
    )

def main():
    st.title("회원 정보를 입력 해주세요")

    # 사용자에게 ID와 비밀번호를 입력받기
    user_id = st.text_input("사용자 ID를 입력하세요:")
    password = st.text_input("비밀번호를 입력하세요:", type="password")

    # 로그인 버튼 클릭 여부 확인
    if st.button("로그인"):
        # 간단한 예제로 사용자 ID가 "user"이고 비밀번호가 "password"일 때만 로그인 성공으로 간주
        if user_id == "user" and password == "password":
            st.success("반가워요!")
            st.link_button("Home","streamlit_app.py")
        else:
            st.error("로그인 실패. 올바른 사용자 ID와 비밀번호를 입력하세요.")

    d = st.date_input("When are you drive?", value=None)
    st.write('Your drive day is:', d)

if __name__ == "__main__":
    main()