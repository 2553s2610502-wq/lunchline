st.markdown("""
<style>

/* 전체 배경 살짝 흐리게 */
.stApp {
    background: linear-gradient(
        rgba(255, 255, 255, 0.92),
        rgba(255, 255, 255, 0.92)
    ),
    url("https://images.unsplash.com/photo-1498837167922-ddd27525d352");
    background-size: cover;
}

/* 제목 귀엽게 */
h1 {
    text-align: center;
    color: #FF6B6B;
    font-size: 42px;
    font-weight: 800;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
}

/* 설명 */
.stMarkdown p {
    text-align: center;
    font-size: 18px;
    color: #555;
}

/* 입력 박스 카드화 */
.block-container {
    background-color: rgba(255,255,255,0.85);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
}

/* 입력창 */
input, .stSelectbox, .stNumberInput {
    border-radius: 12px !important;
}

/* 버튼 (귀엽게 핵심) */
.stButton>button {
    background: linear-gradient(135deg, #FF6B6B, #FFB347);
    color: white;
    font-size: 18px;
    padding: 12px;
    border-radius: 16px;
    border: none;
    width: 100%;
    font-weight: bold;
    box-shadow: 0 4px 10px rgba(0,0,0,0.15);
}

.stButton>button:hover {
    transform: scale(1.03);
    transition: 0.2s;
}

/* 예약 카드 */
.card {
    background: white;
    padding: 15px;
    border-radius: 16px;
    margin: 8px 0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    border-left: 6px solid #FF6B6B;
    font-size: 16px;
}

/* 섹션 제목 */
h2, h3 {
    color: #333;
}

</style>
""", unsafe_allow_html=True)
