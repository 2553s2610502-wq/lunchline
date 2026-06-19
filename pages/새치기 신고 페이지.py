import datetime  # [수정] 모듈 전체를 가져오는 방식이 Streamlit 환경에서 훨씬 안정적입니다.
import streamlit as st

st.set_page_config(page_title="익명 새치기 신고 시스템")

st.title("🚨 급식 새치기 익명 신고 시스템")
st.write("신고자는 익명으로 처리되며 기록만 저장됩니다.")

# -----------------------------
# 데이터 저장 (세션 초기화)
# -----------------------------
if "reports" not in st.session_state:
    st.session_state.reports = []

if "report_count" not in st.session_state:
    st.session_state.report_count = 0

# -----------------------------
# 입력 폼
# -----------------------------
reporter = st.text_input("신고자 이름 (기록에는 남지 않음)").strip()
target = st.text_input("새치기한 사람 이름").strip()

if st.button("익명 신고하기"):
    if not reporter or not target:
        st.warning("모든 항목을 입력하세요.")
    else:
        st.session_state.report_count += 1

        # 안전하게 현재 시간 문자열 생성
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        st.session_state.reports.append({
            "id": st.session_state.report_count,
            "time": now_time,
            "target": target
        })

        st.success("익명으로 신고가 접수되었습니다!")
        
        # [수정] 데이터 추가 즉시 화면을 새로고침하여 앱이 멈추거나 꼬이는 현상을 완벽히 차단
        st.rerun()

# -----------------------------
# 신고 기록 출력
# -----------------------------
st.write("---")
st.subheader("📜 신고 기록")

if not st.session_state.reports:
    st.info("아직 신고 기록이 없습니다.")
else:
    # 최신 신고가 맨 위에 오도록 역순(reversed) 정렬하여 출력
    for r in reversed(st.session_state.reports):
        st.write(f"🔒 **[익명 신고 {r['id']}]** {r['target']} | {r['time']}")
