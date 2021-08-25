from random import randint
import os
from django.conf import settings
import random
import string

from rest_framework_simplejwt.tokens import RefreshToken


def random_with_n_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def random_with_n_aplha(n):
    return ''.join(random.sample(string.ascii_uppercase +
                                 string.digits, k=n))


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }