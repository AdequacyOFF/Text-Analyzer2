
import os
from flask import Flask, request, make_response
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "C:/Users/User/Desktop/Text-Analyzer2-Files"
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/url', methods=['GET', 'POST'])
def url_parse():
    print ("url_parse()")
    if request.method == 'POST':
        return make_response("URL have been parsed", 200)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
    
@app.route('/filesUpload', methods=['GET', 'POST'])
def upload_file():
    print ("upload_file()")
    if request.method == 'POST':
        if 'files' not in request.files:
            return make_response("No file part", 507)
        print(request.files)
        file = request.files['files']
        print (file)
        if file.filename == '':
            return make_response("No selected file", 507)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return make_response("File have been uploaded", 200)
        return make_response("Invalid extension", 507)
app.run(host='127.0.0.1', port=8080)