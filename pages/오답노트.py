import streamlit as st

st.set_page_config(page_title="오답노트", page_icon="📂", layout="wide")

st.title("📂 오답노트")

if "wrong_questions" not in st.session_state:
    st.warning("오답노트가 없습니다.")
    st.stop()

wrong = st.session_state.wrong_questions

if len(wrong) == 0:
    st.success("🎉 모든 문제를 맞혔습니다!")
    if st.button("🏠 Home"):
        st.switch_page("app.py")
    st.stop()

if "wrong_index" not in st.session_state:
    st.session_state.wrong_index = 0

idx = st.session_state.wrong_index
q = wrong[idx]

st.progress((idx + 1) / len(wrong))
st.subheader(f"오답 {idx+1} / {len(wrong)}")

st.divider()

st.markdown(f"### {q['question']}")

for i, choice in enumerate(q["choices"], start=1):

    if choice == q["my_answer"]:
        st.error(f"❌ {i}. {choice}")

    elif choice == q["correct_answer"]:
        st.success(f"✅ {i}. {choice}")

    else:
        st.write(f"{i}. {choice}")

st.divider()

# ---------------- AI 해설 ----------------

with st.expander("🤖 AI 해설 보기"):

    st.info("""
AI 연결 예정입니다.

프롬프트가 완성되면

• 정답인 이유

• 오답인 이유

• 핵심 개념

• 암기 팁

을 생성합니다.
""")

# ---------------- 다시 풀기 ----------------

with st.expander("🔄 다시 풀기"):

    retry = st.radio(
        "정답을 다시 선택하세요.",
        q["choices"],
        key=f"retry_{idx}"
    )

    if st.button("정답 확인", key=f"check_{idx}"):

        if retry == q["correct_answer"]:
            st.success("⭕ 정답입니다!")

        else:
            st.error("❌ 오답입니다.")
            st.write(f"정답 : **{q['correct_answer']}**")

# ---------------- 유사문제 ----------------

with st.expander("✨ 유사문제 생성"):

    st.info("""
AI 연결 예정입니다.

버튼을 누르면 AI가
비슷한 난이도의 새로운 문제를 생성합니다.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:

    if st.button("⬅ 이전", use_container_width=True):

        if idx > 0:
            st.session_state.wrong_index -= 1
            st.rerun()

with col2:

    if idx == len(wrong)-1:

        if st.button("🏠 Home", use_container_width=True):

            st.session_state.current = 0
            st.session_state.answers = [None] * st.session_state.total_questions
            st.session_state.wrong_index = 0

            st.switch_page("app.py")

    else:

        if st.button("다음 ➡", use_container_width=True):

            st.session_state.wrong_index += 1
            st.rerun()