from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators, RecaptchaField
from wtforms import StringField
from wtforms.fields.choices import RadioField
from wtforms.fields.simple import FileField, PasswordField, BooleanField, TelField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.file import FileRequired


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired("Данные не введены")])
    password = PasswordField('Пароль', validators=[DataRequired("you didn't input anithing")])
    remember = BooleanField('Запомнить меня')


# class SearshForm(FlaskForm):
#     searchbar = StringField()


class VerificationForm(FlaskForm):
    choose = RadioField('Выберите действие', choices=[(True,'Подтвердить валидацию'),(False,'Отклонить')])