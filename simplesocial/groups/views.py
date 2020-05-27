from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse
from django.views.generic import *

# project imports
from simplesocial.groups.models import Group, GroupMember
# Create your views here.

