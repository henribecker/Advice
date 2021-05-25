import environ
from startup.settings.base import *

env = environ.Env()

DEBUG = env.bool('DEBUG', False)

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=['django1-hb.herokuapp.com',])

DATABASES = {
    "default": env.db(),
}