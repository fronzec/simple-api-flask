from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        some_json = request.get_json()
        return jsonify({"data sent": some_json}), 201
    else:
        # By default the response code is 200
        return jsonify({"hello": "world"})


@app.route("/multiply/<int:num>", methods=['GET'])
def get_multiply_by_10(num):
    return jsonify({"result": num * 10})


if __name__ == '__main__':
    app.run(debug=True)
