from flask_wtf import FlaskForm
from wtforms import SelectField,IntegerField,SubmitField, StringField
from wtforms.validators import InputRequired,NumberRange


class ProfileForm(FlaskForm):
    direction = SelectField("Выберите сторону света, в которую желаете отправиться",
                            choices = [("up","Север"),("right","Восток"),("down","Юг"),('left',"Запад")])
    steps = IntegerField("Как далеко планируете продвинуться:",validators = [NumberRange(0,3)])
    submit = SubmitField("В путь!")

class EntryForm(FlaskForm):
    name = StringField(label="Ввведите Ваше имя",validators = [InputRequired()])
    submit = SubmitField("Принять испытание!")