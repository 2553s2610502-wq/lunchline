import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="현재 급식상태 요약",
    page_icon="🍱",
    layout="wide"
)

# -----------------------------
# 기본 스타일
# -----------------------------
st.markdown("""
    <style>
    .status-card {
        padding: 25px;
        border-radius: 15px;
        color: white;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .info-box {
        padding: 18px;
        border-radius: 12px;
        background-color: #f5f5f5;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🍱 현재 급식상태 요약")

st.write("실시간 급식 혼잡 상태를 확인할 수 있습니다.")

# -----------------------------
# 사이드바 설정
# -----------------------------
st.sidebar.header("관리자 설정")

status = st.sidebar.selectbox(
    "현재 상태",
    ["원활", "보통", "혼잡", "매우 혼잡"]
)

waiting_time = st.sidebar.text_input(
    "예상 대기시간(분)",
    placeholder="예: 10"
)

people_count = st.sidebar.number_input(
    "현재 이용 인원",
    min_value=0,
    value=120,
    step=1
)

# -----------------------------
# 상태별 색상
# -----------------------------
status_colors = {
    "원활": "#2ecc71",
    "보통": "#f1c40f",
    "혼잡": "#e67e22",
    "매우 혼잡": "#e74c3c"
}

status_messages = {
    "원활": "바로 이용 가능합니다 😊",
    "보통": "약간의 대기가 있을 수 있습니다 🙂",
    "혼잡": "대기 인원이 많습니다 😥",
    "매우 혼잡": "혼잡도가 매우 높습니다 🚨"
}

# -----------------------------
# 대기시간 처리
# -----------------------------
display_waiting = "-"

if waiting_time.strip():
    try:
        wait_num = int(waiting_time)

        if wait_num < 0:
            display_waiting = "-"
        else:
            display_waiting = f"{wait_num}분"

    except ValueError:
        display_waiting = "-"

# -----------------------------
# 메인 상태 카드
# -----------------------------
st.markdown(
    f"""
    <div class="status-card" style="background-color:{status_colors[status]}">
        현재 상태: {status}<br><br>
        <div style="font-size:20px;">
            {status_messages[status]}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# 정보 영역
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        f"""
        <div class="info-box">
            ⏳ 예상 대기시간<br><br>
            {display_waiting}
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="info-box">
            👥 현재 이용 인원<br><br>
            {people_count}명
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# -----------------------------
# 혼잡도 차트
# -----------------------------
st.subheader("📊 시간대별 예상 혼잡도")

chart_data = pd.DataFrame({
    "시간": [
        "11:00", "11:30", "12:00",
        "12:30", "13:00", "13:30"
    ],
    "혼잡도": [20, 45, 90, 75, 50, 25]
})

fig = px.line(
    chart_data,
    x="시간",
    y="혼잡도",
    markers=True,
    line_shape="spline",
)

fig.update_layout(
    height=400,
    yaxis_title="혼잡도",
    xaxis_title="시간",
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# 하단 안내
# -----------------------------
st.info("관리자 설정값을 변경하면 화면이 즉시 업데이트됩니다.")
