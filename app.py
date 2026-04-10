import streamlit as st
from model import predict_email
from utils import extract_features
from bert_model import predict_email_bert
from model import predict_email


st.set_page_config(page_title="AI Phishing Detector")

st.title("🔐 Advanced AI Phishing Detector")

email = st.text_area("Enter email content:")

if st.button("Analyze"):
    if email.strip() == "":
        st.warning("Enter email text")
    else:
        ml_prob = predict_email(email)
        bert_prob = predict_email_bert(email)

        # Combine predictions
        final_prob = (ml_prob + bert_prob) / 2

        st.subheader("Prediction")

        if final_prob > 0.5:
            st.error(f"⚠️ Phishing ({final_prob*100:.2f}%)")
        else:
            st.success(f"✅ Safe ({(1-final_prob)*100:.2f}%)")

        st.write(f"ML Score: {ml_prob:.2f}")
        st.write(f"BERT Score: {bert_prob:.2f}")