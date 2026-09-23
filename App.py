import streamlit as st

# إعدادات الصفحة والتصميم
st.set_page_config(page_title="مفاجأة خاصة ✨", page_icon="💖", layout="centered")

# إضافة تأثيرات CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
        text-align: center;
    }
    .title-text {
        font-size: 32px;
        font-weight: bold;
        color: #ff758c;
        margin-top: 20px;
        font-family: sans-serif;
    }
    .glowing-heart {
        font-size: 110px;
        margin: 20px 0;
        display: inline-block;
        animation: pulse 0.8s infinite alternate, glow 1.5s infinite alternate;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        100% { transform: scale(1.22); }
    }
    @keyframes glow {
        from { text-shadow: 0 0 10px #ff2a6d, 0 0 20px #ff2a6d, 0 0 30px #ff2a6d; }
        to { text-shadow: 0 0 20px #ff758c, 0 0 40px #ff758c, 0 0 70px #ff758c; }
    }
    .card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(12px);
        border-radius: 20px;
        padding: 25px;
        margin-top: 20px;
        border: 1px solid rgba(255, 255, 255, 0.18);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-text">✨ لديك رسالة سحرية جديدة ✨</div>', unsafe_allow_html=True)
st.markdown('<div class="glowing-heart">💖</div>', unsafe_allow_html=True)

name = st.text_input("اكتب اسمك هنا للاستلام:", placeholder="مثلاً: أحمد")

if name:
    st.balloons()
    st.markdown(f"""
        <div class="card">
            <h2 style="color: #ff758c;">أهلاً بك يا {name}! 👋✨</h2>
            <p style="font-size: 20px; line-height: 1.6;">
                أنشأت هذا الكود خصيصاً لأجلك.. أردت فقط أن أتمنى لك يوماً جميلاً مليئاً بالسعادة والنجاح! 🚀🔥
            </p>
        </div>
    """, unsafe_allow_html=True)

    if st.button("اضغط هنا لمفاجأة ثانية 🎁"):
        st.snow()
        st.toast(f"أنت شخص رائع يا {name}! ⭐")
      
