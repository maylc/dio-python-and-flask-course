from flask_restful import Resource

abilities = ['Python', 'Java', 'PHP']


class Ability(Resource):
    def get(self):
        return abilities
