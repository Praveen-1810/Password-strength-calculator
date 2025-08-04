# model_trainer.py
import random
import string
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def generate_weak_password():
    patterns = [
        ''.join(random.choices(string.ascii_lowercase, k=random.randint(4, 6))),
        ''.join(random.choices('1234567890', k=6)),
        random.choice(["abcabc", "aaaaaa", "qwerty", "iloveyou"])
    ]
    return random.choice(patterns)

def generate_medium_password():
    base = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(6, 8)))
    if random.random() > 0.5:
        base = base.replace(random.choice(base), '@', 1)
    return base

def generate_strong_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=random.randint(12, 16)))

passwords = []
labels = []

for _ in range(1500):
    passwords.append(generate_weak_password())
    labels.append(0)
    passwords.append(generate_medium_password())
    labels.append(1)
    passwords.append(generate_strong_password())
    labels.append(2)

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

features = [extract_features(p) for p in passwords]
df = pd.DataFrame(features)
df['label'] = labels

X = df.drop('label', axis=1)
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, 'password_strength_model.pkl')
print("✅ Model saved as 'password_strength_model.pkl'")
