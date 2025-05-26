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

st.title("🌈 MBTI 기반 앱 센터")
st.markdown("여러 가지 **MBTI 기반 웹앱**을 모아둔 공간이에요! 🎉\n사이드바에서 원하는 앱을 골라보세요! 🐰")

st.info("선택한 앱으로 자동 이동하지 않는다면, Streamlit의 `pages` 폴더 안에 해당 앱 파일이 있는지 확인해주세요. 파일 이름은 반드시 숫자 접두어를 포함해야 합니다. 예: `1_직업추천.py`, `2_퀴즈.py` 등")

if selected_app == "MBTI와 직업 추천 💼":
    st.switch_page("pages/1_MBTI와_직업_추천.py")
elif selected_app == "간단 MBTI 추정 퀴즈 🧩":
    st.switch_page("pages/2_간단_MBTI_추정_퀴즈.py")
elif selected_app == "국가별 MBTI 성향분석 🌍":
    st.switch_page("pages/3_국가별_MBTI_성향분석.py")
elif selected_app == "나와 닮은 수학자는? 🧠":
    st.switch_page("pages/4_나와_닮은_수학자는.py")
elif selected_app == "수학학습 가이드 📘":
    st.switch_page("pages/5_수학학습_가이드.py")
