import streamlit as st
import time

# 🎨 페이지 설정
st.set_page_config(
    page_title="MBTI 공부법 추천기 💡",
    page_icon="📚",
    layout="centered",
)

# 📝 MBTI 공부법 데이터
mbti_study_tips = {
    "INTJ": "📚 전략적으로 계획하고 혼자 조용한 환경에서 공부하세요. 목표 설정이 중요해요! 🎯",
    "INTP": "🧠 논리적 연결을 찾으며 탐구하세요. 추상적인 개념도 깊게 파고들어요! 🔍",
    "ENTJ": "📊 목표를 세우고 효율적으로 정복하세요! 경쟁과 리더십이 동기부여가 돼요! 🚀",
    "ENTP": "💡 새롭고 다양한 방법으로 학습해보세요. 토론과 아이디어 공유도 좋아요! 💬",
    "INFJ": "🌌 깊은 통찰을 활용하세요. 의미를 찾고 감성적인 연결도 공부에 도움돼요. 💖",
    "INFP": "🎨 감성에 호소하는 자료로 공부해보세요. 내면 동기와 연결된 주제에 집중! 🌈",
    "ENFJ": "👥 다른 사람과 함께 공부하며 가르치는 것도 좋아요. 동기부여의 달인! 🔥",
    "ENFP": "🎢 지루함은 금물! 창의적인 방식과 다양한 학습 스타일을 시도해보세요! 🎨",
    "ISTJ": "📅 계획적이고 체계적으로 공부하세요. 리스트와 체크박스가 효과적! ✅",
    "ISFJ": "🧸 친숙한 환경에서 차분히 반복 학습! 누군가를 돕는 것처럼 공부해보세요. 🫶",
    "ESTJ": "🏆 목표 지향적으로 구조화된 계획을 세우고 실천하세요! 💼",
    "ESFJ": "📖 사람들과 어울려 공부하거나 스터디 그룹에 참여하면 효과적이에요! 🤝",
    "ISTP": "🔧 실습과 체험으로 배워보세요! 손으로 직접 해보면 더 잘 기억돼요! 🛠️",
    "ISFP": "🌿 조용하고 편안한 분위기에서 감각적인 자료로 학습해보세요. 🍵",
    "ESTP": "⚡ 즉각적인 피드백과 도전 과제가 동기부여가 돼요! 몸으로 배우자! 🏃",
    "ESFP": "🎤 활발한 환경에서 게임처럼 즐기며 공부하세요! 경험이 최고의 교사! 🎭",
}

# 🧠 타이틀
st.markdown("<h1 style='text-align: center;'>MBTI 공부법 추천기 💡</h1>", unsafe_allow_html=True)
st.markdown("### 당신의 MBTI 유형은 무엇인가요? 🤔")

# 🎯 MBTI 선택 드롭다운
mbti_types = list(mbti_study_tips.keys())
user_mbti = st.selectbox("MBTI 유형을 선택하세요 🧬", mbti_types)

# 버튼
if st.button("공부법 추천 받기 🚀"):
    with st.spinner("당신에게 꼭 맞는 공부법을 찾고 있어요... 🧭"):
        time.sleep(2)  # 약간의 딜레이로 긴장감 UP

    # 추천 결과 출력
    st.success(f"🎉 {user_mbti} 유형에게 추천하는 공부법 🎓")
    st.markdown(f"### {mbti_study_tips[user_mbti]}")

    # 🎉 애니메이션 이펙트 (풍선 효과)
    st.balloons()

# 🐾 푸터
st.markdown("---")
st.markdown("<p style='text-align: center;'>만든이: 당신의 AI 도우미 🤖 | 재미로만 봐주세요 😄</p>", unsafe_allow_html=True)

