from flask_restx import Resource, Namespace
from dao.model.director_schema import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return directors_schema.dump(director_service.get_directors()), 200


@director_ns.route('/<int:did>')
class DirectorsView(Resource):
    def get(self, did: int):
        return director_schema.dump(director_service.get_director_by_id(did)), 200
