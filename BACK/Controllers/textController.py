from flask import request, Response
from NeuralNetwork.sentiment_classifier import SentimentClassifier
from NeuralNetwork.JsonMaker import makeJson

def text_process():
    text = request.json.get('inputValue', None)
    classifier = SentimentClassifier()
    result, total_probs = classifier.summary(text)
    return Response(makeJson(result, total_probs), content_type="application/json")
