from flask import Flask, request
from flask_restful import Resource, Api

from models import People, Activities

app = Flask(__name__)
api = Api(app)


class Person(Resource):
    def get(self, name):
        person = People.query.filter_by(name=name).first()

        try:
            response = {
                'name': person.name,
                'age': person.age,
                'id': person.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'message': 'Person not found.'
            }

        return response

    def put(self, name):
        person = People.query.filter_by(name=name).first()
        info = request.json

        if 'name' in info:
            person.name = info['name']

        if 'age' in info:
            person.age = info['age']

        person.save()

        response = {
            'name': person.name,
            'age': person.age,
            'id': person.id
        }

        return response

    def delete(self, name):
        person = People.query.filter_by(name=name).first()
        person.delete()
        message = 'Person excluded successfully. Name: {}'.format(person.name)
        return {'status': 'success', 'message': message}


class ListPeople(Resource):
    def get(self):
        people = People.query.all()
        response = [{'id': i.id, 'name': i.name, 'age': i.age} for i in people]
        return response

    def post(self):
        info = request.json
        person = People(name=info['name'], age=info['age'])
        person.save()

        response = {
            'name': person.name,
            'age': person.age,
            'id': person.id
        }

        return response


class ListActivities(Resource):
    def get(self):
        activities = Activities.query.all()
        response = [{'id': i.id, 'name': i.name, 'person': i.person.name} for i in activities]
        return response

    def post(self):
        info = request.json

        name = info['person']
        person = People.query.filter_by(name=name).first()

        activity = Activities(name=info['name'], person=person)
        activity.save()

        response = {
            'person': activity.person.name,
            'name': activity.name,
            'id': activity.id
        }

        return response


api.add_resource(Person, '/person/<string:name>/')
api.add_resource(ListPeople, '/person/')
api.add_resource(ListActivities, '/tasks/')

if __name__ == '__main__':
    app.run(debug=True)
