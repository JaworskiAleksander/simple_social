from django.db import models
from django.urls import reverse
from django.conf import settings

import misaka

from simplesocial.groups.models import Group

from django.contrib.auth import get_user_model
# connect with model
User = get_user_model()
# Create your models here.

class Post(models.Model):
    # attributes


    # string representation


    # save()


    # get_absolute_url - where to redirect user once a post has been sent successfuly
    pass