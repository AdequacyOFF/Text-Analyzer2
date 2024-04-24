from Controllers.fileController import file_process
from Controllers.urlController import url_process
from Controllers.textController import text_process
from flask import Flask

UPLOAD_FOLDER = "C:/Users/User/Desktop/Text-Analyzer2-Files"
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/text', methods=['GET', 'POST'])
def text_processing():
    text_process()

@app.route('/url', methods=['GET', 'POST'])
def url_processing():
    url_process()

@app.route('/filesUpload', methods=['GET', 'POST'])
def file_processing():
    return file_process(app.config['UPLOAD_FOLDER'], ALLOWED_EXTENSIONS)

app.run(host='127.0.0.1', port=8080)