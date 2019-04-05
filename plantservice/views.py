# Import SQLAlchemy ModelView.
from flask_admin.contrib.sqla import ModelView


class PlantView(ModelView):
    """Extend the ModelView class for Plant models."""


class FamilyView(ModelView):
    """Extend the ModelView class for Family models."""


class GenusView(ModelView):
    """Extend the ModelView class for Genus models."""


class SpeciesView(ModelView):
    """Extend the ModelView class for Species models."""
