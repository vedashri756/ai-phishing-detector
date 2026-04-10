from transformers import pipeline

# Load model (this one is stable)
classifier = pipeline(
    "text-classification",
    model="mrm8488/bert-tiny-finetuned-sms-spam-detection"
)

def predict_email_bert(text):
    result = classifier(text)[0]

    label = result["label"].lower()
    score = result["score"]

    # Normalize output
    if "spam" in label:
        return score
    else:
        return 1 - score