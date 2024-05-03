from flask import request, Response
from NeuralNetwork.sentiment_classifier import SentimentClassifier
from NeuralNetwork.JsonMaker import makeJson

def text_process():
    text = request.json.get('inputValue', None)
    classifier = SentimentClassifier()
    return Response(classifier.summary(text), content_type="application/json")
