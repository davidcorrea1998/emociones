$ python3
>>> from emotion_detection import emotion_detector
>>> emotion_detector("I am glad this worked")
{
    'anger': 0.001,
    'disgust': 0.000,
    'fear': 0.002,
    'joy': 0.996,
    'sadness': 0.001,
    'dominant_emotion': 'joy'
}
>>>
