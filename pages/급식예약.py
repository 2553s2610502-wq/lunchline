import streamlit as st

st.set_page_config(
    page_title="급식 예약",
    page_icon="🍱",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        rgba(255,255,255,0.92),
        rgba(255,255,255,0.92)
    ),
    url("https://images.unsplash.com/photo-1498837167922-ddd27525d352");
    background-size: cover;
}

h1 {
    text-align: center;
    color: #FF6B6B;
    font-size: 40px;
    font-weight: bold;
}

.stButton>button {
    background: linear-gradient(135deg, #FF6B6B, #FFB347);
    color: white;
    border-radius: 12px;
    width: 100%;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("🍱 급식 예약 시스템")
