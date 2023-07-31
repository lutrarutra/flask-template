from flask import Blueprint
from flask_restful import Api, Resource

example_bp = Blueprint('example_bp', __name__, url_prefix='/api/example')
api = Api(example_bp)

class ExampleApi(Resource):
    def get(self, name):
        return {'hello': name}
    
    # def post(self, id):
    #     return {'hello': id}
    
    # def put(self):
    #     return {'hello': 'world'}

api.add_resource(ExampleApi, '/<string:name>')