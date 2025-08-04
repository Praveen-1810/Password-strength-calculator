import streamlit as st
import pandas as pd
import string
import joblib
import random

# === Load model ===
model = joblib.load("password_strength_model.pkl")

# === Feature extraction ===
def extract_features(pwd):
    return {
        'length': len(pwd),
        'upper': sum(1 for c in pwd if c.isupper()),
        'lower': sum(1 for c in pwd if c.islower()),
        'digits': sum(1 for c in pwd if c.isdigit()),
        'special': sum(1 for c in pwd if c in string.punctuation),
        'has_repeats': int(len(set(pwd)) < len(pwd)),
        'contains_space': int(' ' in pwd)
    }

# === Predict password strength ===
def check_strength(pwd):
    feats = extract_features(pwd)
    pred = model.predict(pd.DataFrame([feats]))[0]
    return pred

# === Password Generator ===
def generate_password(strength):
    if strength == 'Weak':
        return ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 6)))
    elif strength == 'Medium':
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    else:
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choices(chars, k=14))

# === UI Styling ===
st.set_page_config(page_title="Password Strength Inspector", layout="centered")

st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #1f1c2c, #928dab);
}
.glass {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(10px);
    padding: 2rem;
    border: 1px solid rgba(255, 255, 255, 0.2);
    animation: float 3s ease-in-out infinite;
}
@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
  100% { transform: translateY(0px); }
}
h1, h2, label, p {
    color: white !important;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# === Heading with Typing Effect ===
st.markdown("<div class='glass'><h1>💥 Password Strength Inspector 💻</h1>", unsafe_allow_html=True)
st.markdown("### *'Is your password ready to fight hackers or toddlers?' 😎*")

# === Password Input Field ===
pwd = st.text_input("🔐 Enter your secret password", type="password")

# === Password Generator Buttons ===
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🎲 Generate Weak"):
        pwd = generate_password('Weak')
with col2:
    if st.button("🎲 Generate Medium"):
        pwd = generate_password('Medium')
with col3:
    if st.button("🎲 Generate Strong"):
        pwd = generate_password('Strong')

# === Emoji Reactions ===
jokes = {
    0: "💀 That's weaker than my grandma's WiFi password!",
    1: "🧐 Decent effort. But still crackable by a caffeine-fueled hacker.",
    2: "🧠 Hacker be like: 'I'm outta here!'"
}
emojis = {
    0: "🟥 Weak",
    1: "🟨 Medium",
    2: "🟩 Strong"
}

# === Show Results ===
if pwd:
    st.markdown(f"<br><h3 style='color:white;'>🔍 Checking strength for:</h3><p style='color:lime;'>{pwd}</p>", unsafe_allow_html=True)
    pred = check_strength(pwd)
    strength = emojis[pred]
    st.markdown(f"<h2>{strength}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p>{jokes[pred]}</p>", unsafe_allow_html=True)

    if pred == 2:
        st.balloons()  # 🎈 confetti celebration for strong passwords

# === Footer ===
st.markdown("""
    <hr>
    <center><p style='color:white;'>Made with 💻, 😂, and a touch of 🔐 by <b>Praveen</b></p></center>
    </div>
""", unsafe_allow_html=True)
