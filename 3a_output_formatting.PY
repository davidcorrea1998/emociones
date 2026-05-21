from transformers import pipeline

emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

def emotion_detector(text_to_analyze):
    scores = emotion_classifier(text_to_analyze)[0]

    emotions = {}
    for score in scores:
        emotions[score['label']] = round(score['score'], 3)

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }
