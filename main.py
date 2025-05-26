import streamlit as st

st.set_page_config(page_title="MBTI 앱 센터 💖", page_icon="🌟", layout="centered")

st.sidebar.title("📚 MBTI 프로그램 모음")
selected_app = st.sidebar.radio(
    "👀 관심 있는 앱을 골라보세요!",
    [
        "MBTI와 직업 추천 💼",
        "간단 MBTI 추정 퀴즈 🧩",
        "국가별 MBTI 성향분석 🌍",
        "나와 닮은 수학자는? 🧠",
        "수학학습 가이드 📘"
    ]
)

st.title("🌈 MBTI 기반 귀여운 앱 센터")
st.markdown("여러 가지 **MBTI 기반 웹앱**을 모아둔 공간이에요! 🎉\n사이드바에서 원하는 앱을 골라보세요! 🐰")

if selected_app == "MBTI와 직업 추천 💼":
    st.markdown("자신의 MBTI에 딱 맞는 직업을 추천해드려요! 어떤 전공이 어울리는지도 함께 알려줘요 ✨")
elif selected_app == "간단 MBTI 추정 퀴즈 🧩":
    st.markdown("몇 가지 간단한 질문으로 MBTI를 빠르게 추정해보는 퀴즈예요! 정확도는 가볍게 즐겨요 🎯")
elif selected_app == "국가별 MBTI 성향분석 🌍":
    st.markdown("전 세계 사람들은 어떤 MBTI가 많을까? 나라별 통계와 함께 성향을 비교해볼 수 있어요 🌐")
elif selected_app == "나와 닮은 수학자는? 🧠":
    st.markdown("당신의 MBTI와 성향을 기반으로, 역사 속 수학자 중 누가 가장 닮았는지 알려드려요! 🧮")
elif selected_app == "수학학습 가이드 📘":
    st.markdown("MBTI 유형별로 맞춤형 수학 학습 전략을 제안해요! 슬럼프 극복에도 도움을 줄 수 있어요 📈")

st.info("🐣 더 많은 귀여운 MBTI 앱이 추가될 예정이에요. 기대해주세요!")
