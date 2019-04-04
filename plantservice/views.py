# Import SQLAlchemy ModelView.
from flask_admin.contrib.sqla import ModelView


class PlantView(ModelView):
    """Extend the ModelView class for Plant models."""
