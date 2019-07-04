from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from music.models import Profile

User = get_user_model()

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30,required=False,help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254,help_text='Required. Inform a valid email address.')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name','address','city','description', 'image' )