from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators, RecaptchaField
from wtforms import StringField
from wtforms.fields.choices import RadioField
from wtforms.fields.simple import FileField, MultipleFileField, PasswordField, BooleanField, TelField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.file import FileRequired


class RegistrationCommonForm(FlaskForm):
    
    # username = StringField('Логин*', validators=[DataRequired("Данные не введены")])
    # last_name = StringField('Фамилия*', validators=[DataRequired('Вы не ввели Фамилию')])
    # first_name = StringField('Имя*', validators=[DataRequired('Вы не ввели имя')])
    # fat_name = StringField('Отчество')
    email = StringField('email*', validators=[DataRequired("Ничего не введено"), Email('Неверный формат')])
    phone = TelField('Введите номер телефона*', validators=[DataRequired('Не введен номер телефона')])
    password = PasswordField('Пароль*', validators=[Length(6, 100, "Пароль должен быть от 6 до 100 символов"), DataRequired()])
    password_repl = PasswordField('Потдвердите пароль*', validators=[EqualTo('password', "Пароли не совпали")])
    role = RadioField("В качестве кого Вы хотите зарегистрироваться?", choices=[(True, 'Супервизор'),(False, "Клиент")])
    # sertificate = FileField('Прикрепите сертификат*', validators=[FileRequired("Файл не прикреплен")])
    # recaptcha = RecaptchaField()


class RegistrationClientField(FlaskForm):
    last_name = StringField('Фамилия*', validators=[DataRequired('Вы не ввели Фамилию')])
    first_name = StringField('Имя*', validators=[DataRequired('Вы не ввели Имя')])
    fat_name = StringField('Отчество')
    sertificate = MultipleFileField('Прикрепите сертификаты*')



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired("Данные не введены")])
    password = PasswordField('Пароль', validators=[DataRequired("you didn't input anithing")])
    remember = BooleanField('Запомнить меня')