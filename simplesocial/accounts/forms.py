# returns user model that is currently active in use
from django.contrib.auth import get_user_model

# user creatin form is already built-in
# handles everything that's needed to create user
# auth.models.User is created properly with this thing
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    class Meta:
        # full list of available fields:
        # https://docs.djangoproject.com/en/3.0/ref/contrib/auth/
        # under User model description
        # https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # customization labels
        self.fields['username'] = 'Display Name'
        self.fields['email'] = 'Email Address'