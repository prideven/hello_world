from flask import Flask, request, session, Response, jsonify  # import flask

apps= Flask(__name__)

@apps.route("/")
def hello():  # call method hello
    return "Hello World!"


if __name__ == '__main__':
    apps.debug = True
    apps.run(host='127.0.0.1', port=8080)
