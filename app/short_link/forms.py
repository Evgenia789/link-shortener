from flask_wtf import Form
from wtforms import StringField

from wtforms.validators import DataRequired


class LinkCreateForm(Form):
    long_url = StringField('Исходный url',
        [
            DataRequired(message="Поле обязательно для заполнения")
        ],
        description="Название")
