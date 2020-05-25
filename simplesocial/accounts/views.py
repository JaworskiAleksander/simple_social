# django imports
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

# project/app imports
from . import forms

# Create your views here.
class SignUp(CreateView):
    pass