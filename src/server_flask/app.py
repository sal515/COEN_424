from flask import Flask
from flask import request

from flask import jsonify

from main import *

# import requests

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return f"Hello World!"


@app.route("/post_test", methods=['POST'])
def json_request():
    # header = request.headers
    user_request = request.json
    response_data = generate_batch_data_response(user_request)
    return jsonify(response_data)
    # return f"Received request"


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=80, debug=False)
    app.run()
