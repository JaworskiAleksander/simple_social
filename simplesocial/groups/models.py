from django.db import models
from django.urls import reverse
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
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # remove non-alphanumeric symbols, lowercase everything, put dashes instead of whitespaces
        self.slug = slugify(self.name)
        # in case we have a markdown group description:
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"pk": self.pk, 'slug': self.slug})

    class Meta:
        ordering = ['name']
    

class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_groups', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')