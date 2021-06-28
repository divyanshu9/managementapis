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
    return ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=n))


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def geturl():
    file_folder = os.path.join(settings.BASE_DIR)
    file_create = os.path.join(file_folder, ".env")
    name = open(file_create, "r")
    lines = name.readlines()
    k = 0
    while k < len(lines):
        lines[k] = lines[k].strip()
        k += 1
    return lines[0], lines[1]
