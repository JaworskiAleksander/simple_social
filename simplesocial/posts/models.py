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
    user = models.ForeignKey(User, related_name='posts')
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts', null=True, blank=True)

    # string representation
    def __str__(self):
        return self.message

    # save()
    def save(self, *args, **kwargs):
        # when someone writes with markdown or posts a link, it'll be formatted properly
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    # get_absolute_url - where to redirect user once a post has been sent successfuly
    def get_absolute_url(self):
        return reverse(
                       "posts:single",
                       kwargs={
                               "pk": self.pk,
                               "username": self.user.username
                               }
                       )
