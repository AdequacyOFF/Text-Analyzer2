from flask import request, make_response
def text_process():
    print ("text_process()")
    print(request.json())
    return make_response("text huekst", 200)