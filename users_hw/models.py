from django.db import models
from django.contrib.auth.models import User

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

class UserHw(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    user_type = models.IntegerField(choices= USER_TYPE , verbose_name='Тип пользователя',
                                    default=ASSISTANT)
    phone_number = models.CharField('phone_number',max_length=100)
    age = models.IntegerField()
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Gender')
    subject = models.IntegerField(choices=SUBJECT, verbose_name='Subject',default=ALGEBRA)

