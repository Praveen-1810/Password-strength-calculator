# 💪 Password Strength Calculator (ML-Based)

This is a machine learning–powered password strength analyzer that evaluates your password as **Weak**, **Medium**, or **Strong** — with a rugged UI, live suggestions, and a real-time generator.

![screenshot](https://raw.githubusercontent.com/Praveen-1810/Password-strength-calculator/main/screenshot.png) <!-- Optional if you want to add image -->

## 🚀 Features

- 🔐 ML model trained with Scikit-learn
- 🧠 Live strength detection with Streamlit
- 🔎 Suggestions while typing (uppercase, special, etc.)
- ⚙️ Password Generator: Weak / Medium / Strong
- 🧱 Dark, rugged 3D-style UI for maximum impact

## 🛠 Tech Stack

- Python
- scikit-learn
- Streamlit
- joblib
- pandas

## 🧠 How It Works

1. `model_trainer.py`: Trains the ML model on synthetic password data.
2. `app.py`: Web interface using Streamlit.
3. The model analyzes password features like:
   - Length
   - Uppercase/lowercase/special/digits
   - Repeated characters
   - Space inclusion

## 🚀 Run Locally

```bash
git clone https://github.com/Praveen-1810/Password-strength-calculator.git
cd Password-strength-calculator

# Install dependencies
pip install -r requirements.txt

# Train the model (one time)
python model_trainer.py

# Run the app
streamlit run app.py
