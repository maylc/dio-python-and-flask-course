from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route("/<int:id>")
def person(id):
    return jsonify({'id': id, 'name': 'John', 'position': 'Software Developer'})


@app.route('/calculate/<int:val1>/<int:val2>')
def calculate(val1, val2):
    return jsonify({'sum': val1 + val2})


@app.route('/calculate', methods=['POST'])
def calculate_new():
    data = json.loads(request.data)
    total = sum(data['numbers'])
    return jsonify({'sum': total})


if __name__ == '__main__':
    app.run(debug=True)
