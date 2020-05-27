from django.db import models
# use slugify to remove any non-alphanumeric characters
# lowercase and add dashes instead of whitespaced
from django.utils.text import slugify

# markdown parsing library
import misaka

# import user model that is actively used in this project
from django.contrib.auth import get_user_model
# Create your models here.
