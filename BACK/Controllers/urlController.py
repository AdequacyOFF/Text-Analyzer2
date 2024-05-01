from flask import request, Response
from Parser.Parser import parse_url
from NeuralNetwork.sentiment_classifier import SentimentClassifier
from NeuralNetwork.JsonMaker import makeJson

def url_process():
    url = request.data
    print(url)
    text = parse_url(url)
    classifier = SentimentClassifier()
    result, total_probs = classifier.summary(text)
    return Response(makeJson(result, total_probs), content_type="application/json")
