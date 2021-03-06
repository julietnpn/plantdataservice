# Import SQLAlchemy ModelView.
from flask_admin.contrib.sqla import ModelView


class PlantView(ModelView):
    """Extend the ModelView class for Plant models."""

    # Do not allow adding/editing/deleting records through the UI.
    can_create = False
    can_edit = False
    can_delete = False

    # Display the "Common name" first in the columns and form.
    column_list = (
        'common_name',
        'family',
        'genus',
        'species'
    )
    form_columns = column_list


class FamilyView(ModelView):
    """Extend the ModelView class for Family models."""


class GenusView(ModelView):
    """Extend the ModelView class for Genus models."""


class SpeciesView(ModelView):
    """Extend the ModelView class for Species models."""
