from os.path import isfile
from shutil import copy


def run():
    if not isfile(".env") and isfile('.env.example'):
        copy('.env.example', '.env')
