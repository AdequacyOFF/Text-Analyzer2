from flask import request, make_response

def url_process():
    print ("url_parse()")
    if request.method == 'POST':
        return make_response("URL have been parsed", 200)