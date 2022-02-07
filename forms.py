from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField,SelectField,DateField
from wtforms.validators import DataRequired


class ToDo(FlaskForm):
    task_name = StringField("Task Name:", validators = [DataRequired()])
    asined_chose = [("",""),(1,"Mark"),(2,"Andrew"), (3,"Elizabeth"), (4,"Kate")]
    asined_to = SelectField("Asined To:", choices=asined_chose, validate_choice=False)
    due_by = DateField("Due By:", validators = [DataRequired()], format = '%d/%m/%Y')
    submit = SubmitField("Submit")