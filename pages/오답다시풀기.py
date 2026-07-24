import streamlit as st
import ast
from database import get_wrong_questions
from ai_service import generate_ai_explanation


st.set_page_config(
    page_title="오답 다시풀기",
    page_icon="📝",
    layout="wide"
)

st.title("📝 오답 다시풀기")

if "selected_exam" not in st.session_state:
    st.warning("선택된 시험이 없습니다.")
    st.stop()

exam_id = st.session_state.selected_exam

questions = get_wrong_questions(exam_id)

if len(questions) == 0:
    st.warning("오답이 없습니다.")
    st.stop()

if "retry_index" not in st.session_state:
    st.session_state.retry_index = 0

idx = st.session_state.retry_index

question, choices, my_answer, correct_answer, explanation = questions[idx]

choices = ast.literal_eval(choices)

st.progress((idx + 1) / len(questions))

st.subheader(f"문제 {idx+1} / {len(questions)}")

st.write(question)

answer = st.radio(
    "정답을 선택하세요.",
    choices,
    index=None,
    key=f"retry_{idx}"
)

if st.button("정답 확인"):

    if answer == choices[correct_answer]:
        st.success("정답입니다!")

    else:
        st.error("오답입니다.")
        st.write(f"정답 : {choices[correct_answer]}")

st.divider()

if st.button("🤖 AI 해설 생성"):

    with st.spinner("AI가 해설을 생성하는 중입니다..."):

        import time
        time.sleep(2)

    result = generate_ai_explanation(
        question,
        choices,
        correct_answer,
        my_answer
)
    st.success("AI 해설 생성 완료!")
    


    st.markdown(result)

st.divider()

if st.button("🔄 유사문제 생성"):

    with st.spinner("AI가 유사문제를 생성하는 중입니다..."):

        import time
        time.sleep(2)

        st.success("유사문제 생성 완료!")

        st.markdown("## 🔄 유사문제")

        st.markdown("""
### 문제

시퀀스 밸브의 특징으로 알맞은 것은?

① 압력을 일정하게 유지한다.

② 유체의 역류를 방지한다.

③ 설정 압력 이상에서 다음 회로를 작동시킨다.

④ 유량을 조절한다.

---
""")

        user_answer = st.radio(
    "답을 선택하세요.",
    ["①", "②", "③", "④"],
    index=None
)

    if st.button("정답 보기"):

        st.success("정답 : ③")

        st.markdown("""
### 📝 해설

시퀀스 밸브는 설정 압력 이상이 되면
다음 회로를 순차적으로 작동시키는
압력 제어 밸브입니다.
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:

    if idx > 0:
        if st.button("⬅ 이전"):
            st.session_state.retry_index -= 1
            st.rerun()

with col2:

    if st.button("📂 오답노트"):

        st.session_state.retry_index = 0
        st.switch_page("pages/오답노트.py")

with col3:

    if idx < len(questions)-1:

        if st.button("다음 ➡"):

            st.session_state.retry_index += 1
            st.rerun()

    else:

        if st.button("✅ 종료"):

            st.session_state.retry_index = 0
            st.switch_page("pages/오답노트.py")