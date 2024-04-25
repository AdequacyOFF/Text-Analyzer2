from flask import request, Response
from Parser.Parser import parse_url
from NeuralNetwork.sentiment_classifier import SentimentClassifier

def url_process():
    url = request.json.get('inputValue', None)
    print(url)
    text = parse_url(url)
    print(text)
    classifier = SentimentClassifier()
    result, total_probs = classifier.summary(text)
    print(result)
    return Response(str(result))
