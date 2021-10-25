from flask import Flask, request
from flask_restful import Resource, Api
from ability import Ability
import json

app = Flask(__name__)
api = Api(app)

developers = [
    {"id": "0", "name": "Rafael", "abilities": ["Python", "Flask"]},
    {"id": "1", "name": "Mary", "abilities": ["Python", "Django"]}
]


class Developer(Resource):
    def get(self, id):
        try:
            response = developers[id]
        except IndexError:
            message = 'Developer not found for id {}'.format(id)
            response = {'status': 'error', 'message': message}
        except Exception:
            response = {'status': 'error', 'message': 'Something went wrong. Please try again later.'}
        return response

    def put(self, id):
        info = json.loads(request.data)
        developers[id] = info
        return info

    def delete(self, id):
        developers.pop(id)
        return {'status': 'success', 'message': 'user deleted successfully!'}


class DeveloperList(Resource):
    def get(self):
        return developers

    def post(self):
        info = json.loads(request.data)
        position = len(developers)
        info['id'] = position
        developers.append(info)
        return developers[position]


api.add_resource(Developer, '/dev/<int:id>')
api.add_resource(DeveloperList, '/dev')
api.add_resource(Ability, '/abilities')

if __name__ == '__main__':
    app.run(debug=True)
