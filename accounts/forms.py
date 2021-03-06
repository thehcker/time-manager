from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import User
from music.models import Profile
from django.db import transaction

# User = get_user_model()

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30,required=False,help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254,help_text='Required. Inform a valid email address.')

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	@transaction.atomic
	def save(self):
		user = super().save(commit=False)
		user.is_user = True
		user.save()

		return user



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name','address','city','description', 'image' )