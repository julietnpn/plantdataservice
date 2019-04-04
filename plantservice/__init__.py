# Import Flask.
from flask import Flask

# Import Flask Admin.
from flask_admin import Admin

# Import SQLAlchemy.
from flask_sqlalchemy import SQLAlchemy

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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.instance_path + '/' + app.config['DATABASE_FILENAME']
db = SQLAlchemy(app)

# Create the database tables, if necessary.
models.Base.metadata.create_all(db.engine)

# Create a Flask Admin interface.
service_name = 'Plant Service'
index_name = 'Plants'
index_view = views.PlantView(models.Plant, db.session, name=index_name, endpoint='admin')
admin = Admin(app, name=service_name, template_mode='bootstrap3', url='/', index_view=index_view)
admin.add_view(views.FamilyView(models.Family, db.session))
admin.add_view(views.GenusView(models.Genus, db.session))
admin.add_view(views.SpeciesView(models.Species, db.session))
