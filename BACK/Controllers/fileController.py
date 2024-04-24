import os
from flask import request, make_response
from werkzeug.utils import secure_filename

def allowed_file(filename, allowedExtensions):
    return '.' in filename and filename.rsplit('.', 1)[1] in allowedExtensions

def file_process(uploadFolder, allowedExtensions):
    print ("upload_file()")
    if request.method == 'POST':
        if 'files' not in request.files:
            return make_response("No file part", 507)
        print(request.files)
        file = request.files['files']
        print (file)
        if file.filename == '':
            return make_response("No selected file", 507)
        if file and allowed_file(file.filename, allowedExtensions):
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(uploadFolder, filename))
            return make_response("File have been uploaded", 200)
        return make_response("Invalid extension", 507)