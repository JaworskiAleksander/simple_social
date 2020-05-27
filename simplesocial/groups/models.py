from django.db import models
# use slugify to remove any non-alphanumeric characters
# lowercase and add dashes instead of whitespaced
from django.utils.text import slugify

# markdown parsing library
import misaka

# import user model that is actively used in this project
from django.contrib.auth import get_user_model
User = get_user_model()

# using custom template tags
from django import template
register = template.Library()

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_lengt=255, unique=True)

class GroupMember(models.Model):

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')