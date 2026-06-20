import os
from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host=os.environ.get('REDIS_HOST','redis'),
port = int(os.environ.get('REDIS_PORT',6379)))

@app.route('/')

def hello_world():
    return "hello from world"

@app.route('/counter')
def rediscounter():
    counter = r.incr('counter')
    return f'<h4>this page has been visited for {counter} times</h4>'

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=5000)