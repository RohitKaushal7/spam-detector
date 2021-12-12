from flask import Flask, request
from flask_cors import CORS

from spamDetector.test import test_for_spam

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET','POST'])
def test():
    body = request.get_json()
    message = body['message']
    result = test_for_spam(message)
    return {'result': result, 'body': body}


if __name__ == '__main__':
    app.run(debug=True)
