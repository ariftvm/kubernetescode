from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'arif Please  subscribe, like, and comment on this video, TY!!!'
