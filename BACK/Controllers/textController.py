from flask import request, Response
from NeuralNetwork.sentiment_classifier import SentimentClassifier

def text_process():
    text = request.json.get('inputValue', None)
    print(text)
    classifier = SentimentClassifier()
    result, total_probs = classifier.summary(text)
    print(result)
    return Response(str(result))
