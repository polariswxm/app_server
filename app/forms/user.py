from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

from app.models import User


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(6, 14, message='The length must between 6-14')])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(6, 10, message='The length must between 6-10')])
    confirm = PasswordField('Confirm pwd', validators=[EqualTo('password',message='Password inconsistency')])

    submit = SubmitField('Register')

# username validation
# def validate_username(self, field):
#     if User.query.filter_by(username=field.data).first():
#         raise ValidationError('The Username has been used,please choose another one')


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    submit = SubmitField('Login')
