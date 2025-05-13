import streamlit as st

mbti_jobs = {
    "INTJ": {
        "title": "🧠 전략가형 - INTJ",
        "description": "논리적이고 독립적인 당신에게 어울리는 직업은...",
        "jobs": ["🧪 데이터 사이언티스트", "📊 전략 컨설턴트", "🧬 AI 연구원", "📈 금융 분석가", "📚 교수"]
    },
    "INTP": {
        "title": "🔍 논리술사형 - INTP",
        "description": "지적 호기심이 넘치는 사색가인 당신에게 어울리는 직업은...",
        "jobs": ["🧠 이론 물리학자", "👨‍💻 소프트웨어 엔지니어", "🧪 연구원", "📖 철학자", "👾 게임 개발자"]
    },
    "ENTJ": {
        "title": "🚀 통솔자형 - ENTJ",
        "description": "야망 가득! 리더십 있는 당신에게 어울리는 직업은...",
        "jobs": ["💼 CEO", "📈 경영 전략가", "👩‍⚖️ 변호사", "🧑‍✈️ 파일럿", "🏛️ 정치가"]
    },
    "ENTP": {
        "title": "💡 발명가형 - ENTP",
        "description": "말 잘하고 아이디어 넘치는 당신, 찰떡 직업은...",
        "jobs": ["🎤 방송인", "🎬 크리에이터", "💻 스타트업 창업자", "🧠 마케팅 기획자", "🧩 UX 디자이너"]
    },
    "INFJ": {
        "title": "🌌 옹호자형 - INFJ",
        "description": "직관과 감성이 조화를 이루는 당신에게 어울리는 직업은...",
        "jobs": ["🧘‍♀️ 상담사", "📚 작가", "🧑‍🏫 교육 컨설턴트", "🕊️ 인권운동가", "🎨 예술가"]
    },
    "INFP": {
        "title": "🎨 중재자형 - INFP",
        "description": "이상주의적이고 따뜻한 당신에게 어울리는 직업은...",
        "jobs": ["📖 소설가", "🧘‍♂️ 심리상담가", "🎼 작곡가", "🧚 콘텐츠 디자이너", "🌈 사회복지사"]
    },
    "ENFJ": {
        "title": "🦸‍♀️ 선도자형 - ENFJ",
        "description": "사람을 이끄는 힘이 있는 당신, 잘 맞는 직업은...",
        "jobs": ["🧑‍🏫 교사", "🎙️ 강연가", "🤝 HR 매니저", "🌐 NGO 리더", "📢 홍보 전략가"]
    },
    "ENFP": {
        "title": "🌈 활동가형 - ENFP",
        "description": "열정과 창의력으로 세상을 바꾸는 당신에게 어울리는 직업은...",
        "jobs": ["🎤 방송인", "🎨 아트디렉터", "🧑‍🏫 교육 전문가", "🗣️ 브랜드 마케터", "🌏 국제 NGO 활동가"]
    },
    "ISTJ": {
        "title": "🧱 청렴결백한 논리주의자 - ISTJ",
        "description": "체계적이고 신중한 당신에게 어울리는 직업은...",
        "jobs": ["🧾 회계사", "⚖️ 판사", "💼 사무직 공무원", "📐 토목 엔지니어", "📊 데이터 관리자"]
    },
    "ISFJ": {
        "title": "🕊️ 수호자형 - ISFJ",
        "description": "따뜻하고 헌신적인 당신에게 잘 맞는 직업은...",
        "jobs": ["👩‍⚕️ 간호사", "🏫 초등교사", "🍰 제과제빵사", "🧸 유치원 선생님", "📚 사서"]
    },
    "ESTJ": {
        "title": "🧭 경영자형 - ESTJ",
        "description": "규칙과 질서를 중시하는 당신에게 어울리는 직업은...",
        "jobs": ["📊 관리자", "🏢 기업 간부", "🧑‍✈️ 군 장교", "🗂️ 프로젝트 매니저", "⚖️ 감사관"]
    },
    "ESFJ": {
        "title": "🤝 사교적인 보호자형 - ESFJ",
        "description": "남을 돕고 이끄는 데서 보람을 느끼는 당신에게 어울리는 직업은...",
        "jobs": ["👩‍⚕️ 간호사", "🧑‍🏫 초등교사", "💼 HR 매니저", "🏥 사회복지사", "🍰 베이커리 카페 사장님"]
    },
    "ISTP": {
        "title": "🔧 장인형 - ISTP",
        "description": "실용적이고 분석적인 당신에게는 이런 직업이 찰떡!",
        "jobs": ["👨‍🔧 정비사", "🔍 보안 전문가", "👨‍💻 프로그래머", "🧗‍♂️ 익스트림 스포츠 강사", "🎮 게임 개발자"]
    },
    "ISFP": {
        "title": "🎵 예술가형 - ISFP",
        "description": "감각적이고 조용한 창조자에게 어울리는 직업은...",
        "jobs": ["🎨 화가", "🎼 음악가", "📷 사진작가", "👗 패션 디자이너", "🌿 플로리스트"]
    },
    "ESTP": {
        "title": "⚡ 사업가형 - ESTP",
        "description": "즉흥적이고 에너지 넘치는 당신에게 어울리는 직업은...",
        "jobs": ["📣 광고 AE", "🏃‍♂️ 스포츠 트레이너", "🎙️ 방송 리포터", "🚘 자동차 딜러", "🎮 e스포츠 선수"]
    },
    "ESFP": {
        "title": "🎉 연예인형 - ESFP",
        "description": "사람들과 즐기고 감정을 나누는 걸 좋아하는 당신!",
        "jobs": ["🎭 배우", "🎤 가수", "🎪 이벤트 플래너", "👗 스타일리스트", "🌟 인플루언서"]
    }
}

st.set_page_config(page_title="MBTI 직업 추천기 💼", page_icon="🔮", layout="centered")

st.title("💫 MBTI 기반 직업 추천기")
st.markdown("당신의 **MBTI**는 무엇인가요? 💡\n선택하면 찰떡같은 직업을 추천해드릴게요! 🌟")

selected_mbti = st.selectbox("🧬 MBTI 유형을 선택하세요:", list(mbti_jobs.keys()), index=0)

if selected_mbti:
    info = mbti_jobs[selected_mbti]
    st.header(info["title"])
    st.markdown(f"_{info['description']}_")
    st.subheader("✨ 추천 직업:")
    for job in info["jobs"]:
        st.write(f"- {job}")
    st.balloons()
