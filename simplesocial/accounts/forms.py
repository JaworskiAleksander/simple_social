# returns user model that is currently active in use
from django.contrib.auth import get_user_model

# user creatin form is already built-in
# handles everything that's needed to create user
# auth.models.User is created properly with this thing
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    pass