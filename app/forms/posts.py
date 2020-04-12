from flask_wtf import  FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    content = TextAreaField('', render_kw={'placeholder':'Post new message......'},
                            validators=[DataRequired(),
                            Length(1, 128, message='post something')])
    submit = SubmitField('Publish')
