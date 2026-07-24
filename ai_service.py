def generate_ai_explanation(
    question,
    choices,
    correct_answer,
    user_answer
):
    return f"""
## 🤖 AI 학습 분석

### 📝 ai 해설
'{question}' 문제에 대한 AI 해설입니다.

### 📚 시험 포인트
AI가 시험 포인트를 생성합니다.

### ⚠️ 헷갈리는 개념
AI가 헷갈리는 개념을 설명합니다.

### 💡 암기 팁
AI가 암기 팁을 제공합니다.

"""
