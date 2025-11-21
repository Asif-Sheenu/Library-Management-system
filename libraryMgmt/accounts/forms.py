from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','phone','adress','password1','password2' ]