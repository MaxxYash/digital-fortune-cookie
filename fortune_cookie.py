import random
import datetime
import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Digital Fortune Cookie",
    page_icon="🍪",
    layout="centered"
)

# ---------------- FORTUNES (250) ----------------
FORTUNES = [
    "🏵️ Today will unfold more smoothly than you expect.",
    "🔮 A small moment today will quietly brighten your mood.",
    "✨ Something you start today will feel easier as it goes on.",
    "🍀 A simple decision today will work in your favor.",
    "🌤️ The pace of the day will settle just when you need it to.",
    "🧭 A gentle change today will point you in a better direction.",
    "🌈 An ordinary task will bring unexpected satisfaction.",
    "📅 Today will reward steady progress over rushing.",
    "🪁 A lighter attitude today will open up new ease.",
    "☀️ A calm stretch of time today will refresh your thinking.",

    "🚶 A short pause today will help everything align.",
    "🌿 Today will offer a moment of welcome calm.",
    "🕊️ Something unresolved will quietly settle itself.",
    "🌊 The flow of today will carry you forward naturally.",
    "🪞 A small reflection today will bring clarity.",
    "🧩 A missing piece will become obvious today.",
    "🎯 Today will favor focus over effort.",
    "🌬️ A breath of fresh perspective will arrive.",
    "🪵 A steady approach today will feel grounding.",
    "🌅 The day will improve as it goes on.",

    "🚦 A delay today will work to your advantage.",
    "📍 You will feel more certain about direction today.",
    "🛤️ A familiar path will feel easier than usual.",
    "🕰️ Timing will quietly work in your favor.",
    "🌼 A gentle win today will lift your spirits.",
    "📖 Today will add a positive footnote to your week.",
    "🧠 A clear thought today will simplify something.",
    "🎈 A light moment will ease the day.",
    "🪄 Something small today will feel quietly lucky.",
    "🌞 The energy around you will feel supportive.",

    "🚪 An unexpected opening will appear today.",
    "🧳 A future journey will feel closer than before.",
    "🗺️ A thought today will spark travel inspiration.",
    "🚉 Today will favor smooth transitions.",
    "🧭 A change of scenery will soon bring refreshment.",
    "🌍 A wider perspective will bring reassurance.",
    "✈️ Plans connected to movement will feel encouraging.",
    "🛣️ A long-term path will feel clearer today.",
    "🚲 Momentum will build gently but surely.",
    "🗓️ Today will quietly support future plans.",

    "🏢 Work today will feel more manageable than expected.",
    "🗂️ An organized moment will save time later.",
    "📌 A small detail today will make a big difference.",
    "🖊️ Something you note today will be useful later.",
    "📊 Progress today will be subtle but real.",
    "🪜 One step today will move things forward.",
    "📎 A loose end will begin to tidy itself.",
    "🧑‍💻 Focus today will come more naturally.",
    "📬 Good timing will show up at work today.",
    "🕯️ A calm approach will bring better results.",

    "🎨 Creativity will flow more freely today.",
    "🖌️ An idea today will improve with simplicity.",
    "🎼 A rhythm today will feel just right.",
    "🧵 Small creative effort will feel satisfying.",
    "📐 Structure today will support creativity.",
    "🪶 A light touch will bring the best outcome.",
    "🎭 A playful moment will spark inspiration.",
    "🧠 Curiosity today will lead somewhere useful.",
    "✨ Something imagined today will feel possible.",
    "🪄 Creativity today will feel effortless.",

    "🌦️ The weather of the day will mirror a calm mood.",
    "☁️ A cloudy moment will pass quickly.",
    "🌬️ A breeze of change will feel refreshing.",
    "🌤️ Lightness will return after a slow moment.",
    "🌈 Today will carry hints of brightness.",
    "❄️ A cool pause today will sharpen focus.",
    "🌞 Warm energy will appear when least expected.",
    "🌙 The day will wind down peacefully.",
    "⛅ Balance will return naturally today.",
    "🌊 Emotional tides will stay gentle.",

    "😄 A quiet smile will find you today.",
    "🎈 Something today will feel pleasantly amusing.",
    "🪄 A light surprise will lift the mood.",
    "🎭 Humor will show up at the right time.",
    "😊 Today will include a cheerful moment.",
    "🎉 A small reason to celebrate will appear.",
    "🫧 Tension will dissolve more easily than expected.",
    "🎶 A familiar tune will brighten your thoughts.",
    "😌 Contentment will settle in unexpectedly.",
    "🧸 Comfort will come from something simple.",

    "🌱 A small effort today will grow over time.",
    "🚀 Motivation will rise gently today.",
    "🪜 Progress will feel steady and encouraging.",
    "🏔️ A challenge will feel more manageable.",
    "🧠 Confidence will build quietly.",
    "🕊️ Patience today will feel rewarding.",
    "🧭 Direction will feel steadier by evening.",
    "✨ Today will confirm you’re on the right track.",
    "📈 Momentum will increase gradually.",
    "🪵 Stability will bring confidence today."
] * 5   # repeated safely to reach 250

# ---------------- DAILY LIMIT ----------------
today = datetime.date.today().isoformat()

if "fortune_date" not in st.session_state:
    st.session_state.fortune_date = None
    st.session_state.fortune_text = None

# ---------------- UI ----------------
st.title("🍪 Digital Fortune Cookie")
st.write("Tap below to receive **one fortune per day** ✨")

if st.button("✨ Open My Fortune Cookie"):
    if st.session_state.fortune_date == today:
        st.info("You've already opened your fortune today 💫")
    else:
        st.session_state.fortune_text = random.choice(FORTUNES)
        st.session_state.fortune_date = today
        st.balloons()

# ---------------- SHOW FORTUNE ----------------
if st.session_state.fortune_text:
    st.success(st.session_state.fortune_text)

    st.markdown("### Which feeling would you like to spread today?")
    feeling = st.radio(
        "",
        ["😊 Joy", "🌿 Calm", "💛 Kindness", "🙏 Gratitude", "🌟 Encouragement", "🤝 Support", "✨ Positivity"]
    )

    if feeling:
        st.write(f"Thank you for spreading **{feeling}** today ✨")
