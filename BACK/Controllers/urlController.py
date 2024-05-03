from flask import request, Response
from Parser.Parser import parse_url
from NeuralNetwork.sentiment_classifier import SentimentClassifier
from NeuralNetwork.JsonMaker import makeJson

def url_process():
    url = request.data
    print(url)
    text = parse_url(url)
    classifier = SentimentClassifier()
    return Response(classifier.summary(text), content_type="application/json")
