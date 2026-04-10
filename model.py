import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from utils import extract_features

# Load dataset
df = pd.read_csv("emails.csv", sep="\t", names=["label", "text"])

df["label"] = df["label"].map({"spam": 1, "ham": 0})
df = df.dropna()

# TF-IDF
vectorizer = TfidfVectorizer(stop_words="english", max_features=3000)
X_text = vectorizer.fit_transform(df["text"])

X_text_df = pd.DataFrame(X_text.toarray())
X_text_df.columns = X_text_df.columns.astype(str)

# Extra features
extra = df["text"].apply(extract_features).apply(pd.Series)
extra.columns = extra.columns.astype(str)

# 🔥 BOOST feature importance
extra = extra * 10

# Combine
X = pd.concat([X_text_df, extra], axis=1)
y = df["label"]

# Train
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Accuracy
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")

# =========================
# FINAL PREDICTION FUNCTION
# =========================
def predict_email(text):

    # RULE-BASED OVERRIDE (CRITICAL)
    features = extract_features(text)

    if features["num_suspicious"] >= 2 or features["has_click_phrase"]:
        return 0.9   # force phishing

    # ML prediction
    text_vec = vectorizer.transform([text]).toarray()
    text_df = pd.DataFrame(text_vec)
    text_df.columns = text_df.columns.astype(str)

    extra = pd.DataFrame([features])
    extra.columns = extra.columns.astype(str)
    extra = extra * 10

    final_input = pd.concat([text_df, extra], axis=1)

    prob = model.predict_proba(final_input)[0][1]

    return prob