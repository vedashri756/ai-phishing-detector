import re

def extract_features(text):
    text_lower = text.lower()

    suspicious_words = [
        "urgent", "click", "verify", "password",
        "bank", "account", "login", "confirm",
        "compromised", "security", "alert",
        "immediately", "update", "suspend", "limited"
    ]

    return {
        "length": len(text),
        "num_links": len(re.findall(r'http[s]?://', text)),
        "num_digits": sum(c.isdigit() for c in text),
        "num_caps": sum(c.isupper() for c in text),
        "num_exclamations": text.count("!"),
        "num_suspicious": sum(text_lower.count(word) for word in suspicious_words),
        "has_click_phrase": int("click here" in text_lower)
    }