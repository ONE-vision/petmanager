from flask import Flask
from flask_restx import Api,Resource, fields, reqparse

add_parser=reqparse.RequestParser()
add_parser.add_argument('id', type=int)
add_parser.add_argument('name', type=str)
add_parser.add_argument('species', type=str)
add_parser.add_argument('gender_male', type=bool)
from petmanager import PetManager

app = Flask(__name__)
api = Api(app)
animal=api.model('Animal',
                 {'id': fields.Integer,
                  'name': fields.String,
                  'species': fields.String,
                  'gender_male': fields.Boolean})
app.mgr=PetManager()
@api.route('/api/v1/list')
class List(Resource):
    def get(self,gender=None, species=None):
        return app.mgr.list_animals(gender=gender,species=species)
    
    
@api.route('/api/v1/add')
class Add(Resource):
    @api.expect(animal)

    def post(self):
        args=add_parser.parse_args()
        return app.mgr.add_animal(args)
    
@api.route('/api/v1/get/int:id')
class Get(Resource):
    def get(self,id):
        return app.mgr.get_animal(id)


if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0", port=8888)