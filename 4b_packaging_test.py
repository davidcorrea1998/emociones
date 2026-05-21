$ python3
>>> from EmotionDetection.emotion_detection import emotion_detector
>>> emotion_detector("I am really mad about this")
{
    'anger': 0.946,
    'disgust': 0.012,
    'fear': 0.008,
    'joy': 0.002,
    'sadness': 0.032,
    'dominant_emotion': 'anger'
}
>>>
