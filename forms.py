from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, SelectField, BooleanField, DateField
from wtforms.validators import DataRequired

class NewTask(FlaskForm):
    name = StringField("Task Name:", validators=[DataRequired()])
    user_choices = [("", ""), (1, "Mark"), (2, "Kate"), (3, "Andrew"), (4, "Elizabeth")]
    user_id = SelectField("Assigned to:", choices = user_choices, validate_choice = False)
    date = DateField("Due by:", validators=[DataRequired()], format = '%d/%m/%Y')
    submit = SubmitField("Add New Task")

class DeleteTask(FlaskForm):
    name = StringField("Task Name:", validators=[DataRequired()])
    submit = SubmitField("Delete Task")


