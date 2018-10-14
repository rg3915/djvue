import os
import django
import timeit
from datetime import date, datetime, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

import string
from random import choice, randint, random, sample
from django.contrib.auth.models import User
from django.utils.text import slugify


class Utils:
    ''' Métodos genéricos. '''
    @staticmethod
    def gen_string(max_length):
        '''
        Gera uma string randomica.
        '''
        return str(''.join(choice(string.ascii_letters) for i in range(max_length)))
    gen_string.required = ['max_length']

    @staticmethod
    def gen_date(min_year=2018, max_year=datetime.now().year):
        '''
        Gera um date no formato yyyy-mm-dd.
        '''
        start = date(min_year, 1, 1)
        years = max_year - min_year + 1
        end = start + timedelta(days=365 * years)
        return start + (end - start) * random()

    def gen_digits(max_length):
        return str(''.join(choice(string.digits) for i in range(max_length)))


class UserClass:
    '''
    Métodos pra criar User.
    '''

    @staticmethod
    def create_user1(max_itens=None):
        user = User.objects.create_user(
            username='admin',
            email='admin@email.com',
            first_name='Admin',
            last_name='Admin',
            is_staff=True,
            is_superuser=True,
        )
        user.set_password('d')
        user.save()


tic = timeit.default_timer()

User.objects.all().delete()

UserClass.create_user1()

toc = timeit.default_timer()
print('time', toc - tic)
