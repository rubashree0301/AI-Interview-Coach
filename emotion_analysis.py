from textblob import TextBlob

def analyze_emotion(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Confident / Positive"
    elif polarity < 0:
        return "Nervous / Negative"
    else:
        return "Neutral"