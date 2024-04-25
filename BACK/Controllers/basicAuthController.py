from flask import request, Response

def basic_auth():
    if request.method.lower() == 'options':
        return Response()
    