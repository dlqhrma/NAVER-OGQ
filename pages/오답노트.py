import streamlit as st

st.set_page_config(
    page_title="오답노트",
    page_icon="📂",
    layout="wide"
)

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

st.markdown(f"## {q['question']}")

st.write("")

for i, choice in enumerate(q["choices"], start=1):

    prefix = f"{i}. "

    if choice == q["my_answer"] and choice == q["correct_answer"]:
        st.success(f"✅ {prefix}{choice}")

    elif choice == q["my_answer"]:
        st.markdown(f"❌ **{prefix}{choice}**")

    elif choice == q["correct_answer"]:
        st.markdown(f"✅ **{prefix}{choice}**")

    else:
        st.write(f"{prefix}{choice}")

st.divider()

st.subheader("🤖 AI 해설")

st.info("""
AI가 연결되면

• 정답인 이유

• 오답인 이유

• 핵심 개념

• 암기 팁

을 설명합니다.
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