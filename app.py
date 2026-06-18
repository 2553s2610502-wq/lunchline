import streamlit as st

st.set_page_config(
    page_title="첫 번째 Streamlit 앱",
    page_icon="🚀"
)

st.title("🚀 Streamlit Community Cloud 테스트")

name = st.text_input("이름을 입력하세요")

if name:
    st.success(f"안녕하세요, {name}님!")
else:
    st.info("이름을 입력해 보세요.")
