import streamlit as st

st.set_page_config(
page_title="학교 급식 예약 시스템",
page_icon="🍽️",
layout="centered"
)

st.title("🍽️ 학교 급식 예약 시스템")
st.write("급식을 먹을 학생은 아래 정보를 입력하고 예약하세요!")

if "reservations" not in st.session_state:
st.session_state.reservations = []

with st.form("reservation_form"):
grade = st.selectbox("학년", [1, 2, 3, 4, 5, 6])
classroom = st.number_input("반", min_value=1, max_value=20, step=1)
number = st.number_input("번호", min_value=1, max_value=50, step=1)

```
submit = st.form_submit_button("예약하기")
```

if submit:
student_id = f"{grade}-{classroom}-{number}"

```
existing_ids = [
    item["id"] for item in st.session_state.reservations
]

if student_id in existing_ids:
    st.error("이미 예약한 학생입니다.")
else:
    st.session_state.reservations.append(
        {
            "id": student_id,
            "grade": grade,
            "classroom": classroom,
            "number": number
        }
    )
    st.success("급식 예약이 완료되었습니다! 🎉")
```

st.divider()

st.subheader("📋 현재 예약 현황")

if st.session_state.reservations:
for student in st.session_state.reservations:
st.write(
f"{student['grade']}학년 "
f"{student['classroom']}반 "
f"{student['number']}번"
)

```
st.info(f"총 예약 인원: {len(st.session_state.reservations)}명")
```

else:
st.info("아직 예약한 학생이 없습니다.")

