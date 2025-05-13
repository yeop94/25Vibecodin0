import streamlit as st

# mbti_jobs = { ... } ← 여기에 앞서 만든 전체 16MBTI 딕셔너리를 붙여넣으면 돼

st.set_page_config(page_title="MBTI 직업 추천기 💼", page_icon="🔮", layout="centered")

st.title("💫 MBTI 기반 직업 추천기")
st.markdown("당신의 **MBTI**는 무엇인가요? 💡\n선택하면 찰떡같은 직업을 추천해드릴게요! 🌟")

selected_mbti = st.selectbox("🧬 MBTI 유형을 선택하세요:", list(mbti_jobs.keys()), index=0)

if selected_mbti:
    info = mbti_jobs[selected_mbti]
    
    st.header(info["title"])  # MBTI 유형 이름 + 이모지
    st.markdown(info["description"])  # 성격 특성 설명
    
    st.subheader("✨ 추천 직업:")
    for job in info["jobs"]:
        st.markdown(f"**{job['name']}**")
        st.markdown(f"🧠 추천 이유: {job['reason']}")
        st.markdown(f"🎓 추천 전공: `{job['major']}`")
        st.markdown("---")

    st.success("🎯 당신에게 꼭 맞는 직업이 보이시나요?")
    st.balloons()
