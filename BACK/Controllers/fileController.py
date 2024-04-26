import os
from flask import request, make_response, jsonify
from werkzeug.utils import secure_filename
from NeuralNetwork.sentiment_classifier import SentimentClassifier

def allowed_file(filename, allowedExtensions):
    return '.' in filename and filename.rsplit('.', 1)[1] in allowedExtensions

def file_process(uploadFolder, allowedExtensions):
    if request.method == 'POST':
        if 'files' not in request.files:
            return make_response("No file part", 507)
        file = request.files['files']
        if file.filename == '':
            return make_response("No selected file", 507)
        if file and allowed_file(file.filename, allowedExtensions):
            filename = secure_filename(file.filename)
            file.save(os.path.join(uploadFolder, filename))
            filepath = (uploadFolder +"\\"+ filename).replace('/','\\')
            s_file = open(filepath, encoding='utf-8')
            classifier = SentimentClassifier()
            result, total_probs = classifier.summary(s_file.read())
            return make_response(str(result), 200)
        return make_response("Invalid extension", 507)
    