# django imports
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

# project/app imports
from . import forms

# Create your views here.
class SignUp(CreateView):
    # define which form will be used in this view
    # no parenthesis, I don't want to instantiatize this yet
    form_class = forms.UserCreateForm
    # once someone has successfuly singed up, send them to page that's under 'login' alias name
    # reverse_lazy is executed AFTER submit button is pressed
    success_url = reverse_lazy('login')
    template_name = 'acounts/signup.html'