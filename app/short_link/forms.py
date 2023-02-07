from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class LinkCreateForm(Form):
    """
    Class LinkCreateForm provides field construction,
    validation, and data and error proxying.
    """
    long_url = StringField(label='Long URL', validators=
        [
            DataRequired(message="The field is required to fill in")
        ],
        description="Name")
    short_url = StringField(label='Short URL', description="Name")
