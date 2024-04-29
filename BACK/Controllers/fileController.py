import os
from flask import request, Response
from werkzeug.utils import secure_filename
from NeuralNetwork.sentiment_classifier import SentimentClassifier
from NeuralNetwork.JsonMaker import makeJson

def allowed_file(filename, allowedExtensions):
    return '.' in filename and filename.rsplit('.', 1)[1] in allowedExtensions

def file_process(uploadFolder, allowedExtensions):
    if request.method == 'POST':
        if 'files' not in request.files:
            return Response("No file part", status=507)
        file = request.files['files']
        if file.filename == '':
            return Response("No selected file", status=507)
        if file and allowed_file(file.filename, allowedExtensions):
            filename = secure_filename(file.filename)
            file.save(os.path.join(uploadFolder, filename))
            filepath = (uploadFolder +"\\"+ filename).replace('/','\\')
            s_file = open(filepath, encoding='utf-8')
            classifier = SentimentClassifier()
            result, total_probs = classifier.summary(s_file.read())
            return Response(makeJson(result, total_probs), content_type="application/json")
        return Response("Invalid extension", status=507)
    