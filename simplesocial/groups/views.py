from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse
from django.views.generic import *

# project imports
from simplesocial.groups.models import Group, GroupMember
# Create your views here.

class CreateGroup(LoginRequiredMixin, CreateView):
    # specify fields used to create new group
    # directly linked to Group in groups.models.py
    fields = ('name', 'description')
    model = Group

class SingleGroup(DetailView):
    model = Group

class ListGroup(ListView):
    model = Group