from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired


class GetData(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
