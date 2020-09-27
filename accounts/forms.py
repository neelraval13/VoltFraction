from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import *

class GameForm(ModelForm):
	class Meta:
		model = Tier 
		fields = '__all__'
		#fields =['game','tierlist','played','won']



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User 
		fields = ['username', 'email', 'password1', 'password2']
		
