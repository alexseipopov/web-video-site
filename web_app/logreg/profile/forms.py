from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators, RecaptchaField
from wtforms import StringField
from wtforms.fields.simple import FileField, PasswordField, BooleanField, TelField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.file import FileRequired


class ClientForm(FlaskForm):
    
    username = StringField('Логин*', validators=[DataRequired("Данные не введены")])
    last_name = StringField('Фамилия*', validators=[DataRequired('Вы не ввели Фамилию')])
    first_name = StringField('Имя*', validators=[DataRequired('Вы не ввели имя')])
    fat_name = StringField('Отчество')
    phone = StringField('Введите номер телефона', validators=[DataRequired('Не введен номер телефона')])
    email = StringField('email*', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль*', validators=[Length(6, 100, "Пароль должен быть от 6 до 100 символов"), DataRequired()])
    password_repl = PasswordField('Потдвердите пароль*', validators=[EqualTo('password', "passwords not match")])
    #sertificate = FileField('Прикрепите сертификат*', validators=[FileRequired("Файл не прикреплен")])
    # recaptcha = RecaptchaField()

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired("Данные не введены")], render_kw={'placeholder': 'input user name'})
    password = PasswordField('Пароль', validators=[DataRequired("you didn't input anithing")])
    remember = BooleanField('Запомнить меня')