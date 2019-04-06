# Import Flask.
from flask import Flask

# Import Flask Admin.
from flask_admin import Admin

# Import SQLAlchemy.
from flask_sqlalchemy import SQLAlchemy

# Import Flask-Restful libraries.
from flask_restful import Api, reqparse, abort, Resource

# Import models.
import plantservice.models as models

# Import views.
import plantservice.views as views

# Import default settings.
import plantservice.default_settings

# Create a Flask application.
app = Flask(__name__, instance_relative_config=True)

# Load configuration from defaults first, then override with a settings.py file
# inside the instance path.
app.config.from_object('plantservice.default_settings')
app.config.from_pyfile('settings.py', silent=True)

# Create a database session.
db = SQLAlchemy(app)

# Create the database tables, if necessary.
models.Base.metadata.create_all(db.engine)


def load_plants(session):
    """Load all plants."""
    plants = {}
    for plant in session.query(models.Plant).order_by(models.Plant.common_name).all():
        plants[plant.id] = {
            'common_name': plant.common_name,
            'family': plant.family.name,
            'genus': plant.genus.name,
            'species': plant.species.name,
        }
    return plants

# Create a RESTful API service.
api = Api(app)

# Create a request parser.
parser = reqparse.RequestParser()
parser.add_argument('name')


class Plant(Resource):
    """Individual plant resource."""
    def get(self, plant_id):
        plants = load_plants(db.session)
        if plant_id not in plants:
            abort(404, message="Plant {} doesn't exist".format(plant_id))
        return plants[plant_id]


class PlantList(Resource):
    """Plant list resource."""
    def get(self):
        plants = load_plants(db.session)
        return plants


# Create API resource endpoints.
api.add_resource(PlantList, '/plants')
api.add_resource(Plant, '/plants/<plant_id>')

# Create a Flask Admin interface.
service_name = 'Plant Service'
index_name = 'Plants'
index_view = views.PlantView(models.Plant, db.session, name=index_name, endpoint='admin')
admin = Admin(app, name=service_name, template_mode='bootstrap3', url='/', index_view=index_view)
admin.add_view(views.FamilyView(models.Family, db.session))
admin.add_view(views.GenusView(models.Genus, db.session))
admin.add_view(views.SpeciesView(models.Species, db.session))
