from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from . import models


ADMIN = 1
DIRECTOR = 2
TEACHER = 3
ENGINEER = 4
ASSISTANT = 5

USER_TYPE = (
    (ADMIN, 'ADMIN'),
    (DIRECTOR, 'DIRECTOR'),
    (TEACHER, 'TEACHER'),
    (ENGINEER, 'ENGINEER'),
    (ASSISTANT, 'ASSISTANT')
)

MALE = 1
FEMALE = 2
OTHER = 3

GENDER_TYPE = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE'),
    (OTHER, 'OTHER')
)


ALGEBRA = 1
RUSSIAN_LANGUAGE = 2
HISTORY = 3
ANATOMY = 4
PHYSICS = 5

SUBJECT = (
    (ALGEBRA, 'ALGEBRA'),
    (RUSSIAN_LANGUAGE, 'RUSSIAN'),
    (HISTORY, 'HISTORY'),
    (ANATOMY, 'ANATOMY'),
    (PHYSICS, 'PHYSICS')
)




class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    choic_subject = forms.ChoiceField(choices=SUBJECT, required=True)

    class Meta:
        model = models.UserHw
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "age",
            "user_type",
            "gender",
            "choic_subject"
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm,self).__init__(*args, **kwargs)


    username = UsernameField(widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder':'username',
                'id':'hello'}
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class":'form-control',
            'placeholder':'password',
            'id':'hi'
        }
    ))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "class": 'form-control',
            'placeholder':'email',
            'id':'huh'
        }
    ))







