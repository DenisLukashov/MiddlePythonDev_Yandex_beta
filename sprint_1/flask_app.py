from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/client/info', methods=['GET'])
def user_agent():

    return jsonify({'user_agent': request.headers.get('User-Agent')})


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)
