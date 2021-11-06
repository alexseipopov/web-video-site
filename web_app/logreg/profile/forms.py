from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators, RecaptchaField
from wtforms import StringField
from wtforms.fields.simple import PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegisterForm(FlaskForm):
    
    username = StringField('Логин', validators=[DataRequired("Данные не введены")], render_kw={'placeholder': 'input user name'})
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[Length(6, 100, "Пароль должен быть от 6 до 100 символов"), DataRequired()])
    password_repl = PasswordField('Потдвердите пароль', validators=[EqualTo('password', "passwords not match")])
    # recaptcha = RecaptchaField()

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired("Данные не введены")], render_kw={'placeholder': 'input user name'})
    password = PasswordField('Пароль', validators=[DataRequired("you didn't input anithing")])
    remember = BooleanField('Запомнить меня')