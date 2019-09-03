from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.db import transaction
# from music.models import Profile

# User = get_user_model()

class ManagerSignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30,required=False,help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254,help_text='Required. Inform a valid email address.')

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	@transaction.atomic
	def save(self, commit=True):
		user = super().save(commit=False)
		user.is_super_user = True
		if commit:
			user.save()

		return user



class UserManagerForm(forms.ModelForm):
	class Meta:
		model = User
		fields = '__all__'