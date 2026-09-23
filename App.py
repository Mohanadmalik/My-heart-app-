import random
import time
import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="💍 لعبة النصيب وعروس المستقبل", page_icon="👰‍♂️", layout="centered"
)

# عنوان التطبيق ومقدمة مرحة
st.title("💍 مَخبَر النصيب وعروس المستقبل! 🔮")
st.write(
    "اكتب اسمك يا عريس وسيقوم الذكاء الاصطناعي باختيار عروسة مستقبلك من القائمة العشوائية! 😂✨"
)

# إدخال اسم العريس
groom_name = st.text_input(
    "🕺 اكتب اسمك هنا للبدء:", placeholder="مثلاً: أحمد أو محمد"
)

# قائمة البنات مع تحديد نوع التأثير البصري
brides = [
    {
        "name": "رؤي جمال الخالة 👸✨",
        "comment": "مبروك! الدلع والجمال كله عند الخالة.. جهّز نفسك للزيارات والمناسبات الفخمة!",
        "type": "laugh",
    },
    {
        "name": "نادي محمد همزه العجوز 👵☕",
        "comment": "مبروك! الحكمة والخبرة والوقار كله هنا.. جهّز الشاي والونسات الممتعة طوال الليل!",
        "type": "laugh",
    },
    {
        "name": "ريان السمحة البتجيب الكهرباء ⚡💡",
        "comment": "مبروك! البيت دائماً منوّر.. ومستحيل تنقطع عندكم الكهرباء أو الطاقة الإيجابية!",
        "type": "electric",
    },
]

# زر التشغيل
if st.button("🎲 اكشف نصيبك وعروس مستقبلك الآن!"):
    if not groom_name.strip():
        st.warning("⚠️ يرجى كتابة اسمك أولاً يا عريس!")
    else:
        # تأثير انتظار ومزاح
        with st.spinner("جاري قراءة الفنجان وتحليل كيمياء النصيب... ☕🔮"):
            time.sleep(1.5)

        # اختيار عشوائي
        selected_bride = random.choice(brides)

        # 1. إذا كانت النتيجة (رؤي) أو (نادي) -> ألعاب نارية وضحك شديد
        if selected_bride["type"] == "laugh":
            st.balloons()
            st.error("😂🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣")
            st.success(f"🎉 ألف مبروك يا عريس **{groom_name}**!")
            st.markdown(f"### 👰 عروسة مستقبلك هي: **{selected_bride['name']}**")
            st.info(f"💬 **توقع النصيب:** {selected_bride['comment']}")
            st.write("### 🤣 🤣 🤣 🤣 🤣 🤣 🤣 🤣 🤣 🤣 🤣")

        # 2. إذا كانت النتيجة (ريان) -> تأثير كهرباء وإنارة وتوهج أصفر
        elif selected_bride["type"] == "electric":
            st.snow()  # تأثير بصري شبيه بالتشرذم الكهربائي
            st.warning("⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡")
            st.success(f"🎉 ألف مبروك يا عريس **{groom_name}**!")
            st.markdown(f"### 👰 عروسة مستقبلك هي: **{selected_bride['name']}**")
            st.info(f"💬 **توقع النصيب:** {selected_bride['comment']}")

            # كارت كهربائي منوّر باللون الأصفر
            st.markdown(
                """
                <div style='background-color: #FFE600; padding: 20px; border-radius: 12px; text-align: center; color: #000; font-weight: bold; font-size: 22px; box-shadow: 0px 0px 20px #FFE600;'>
                    💡⚡ تحذير: طاقة كهرومغناطيسية عالية! المكان منوّر 220 فولت ⚡💡
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.write("---")
        st.caption("💡 يمكنك الضغط على الزر مرة أخرى لتجربة نصيبك من جديد!")
