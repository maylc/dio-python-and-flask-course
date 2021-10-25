import json

from flask import Flask, jsonify, request

app = Flask(__name__)

developers = [
    {"id": "0", "name": "Rafael", "abilities": ["Python", "Flask"]},
    {"id": "1", "name": "Mary", "abilities": ["Python", "Django"]}
]


@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def developer(id):
    if request.method == 'GET':
        try:
            response = developers[id]
        except IndexError:
            message = 'Developer not found for id {}'.format(id)
            response = {'status': 'error', 'message': message}
        except Exception:
            response = {'status': 'error', 'message': 'Something went wrong. Please try again later.'}
        return jsonify(response)
    elif request.method == 'PUT':
        info = json.loads(request.data)
        developers[id] = info
        return jsonify(info)
    elif request.method == 'DELETE':
        developers.pop(id)
        return jsonify({'status': 'success', 'message': 'user deleted successfully!'})


@app.route('/dev', methods=['POST', 'GET'])
def list_developers():
    if request.method == 'POST':
        info = json.loads(request.data)
        position = len(developers)
        info['id'] = position
        developers.append(info)
        return jsonify(developers[position])
    elif request.method == 'GET':
        return jsonify(developers)

if __name__ == '__main__':
    app.run(debug=True)
