import os

# Turn off debugging by default.
DEBUG = False

# Set the default database URI.
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

# Define a default secret.
SECRET_KEY = 'secret'

# Configure the Bootstrap theme.
FLASK_ADMIN_FLUID_LAYOUT = True
FLASK_ADMIN_SWATCH = 'flatly'
