from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import SignUpForm

# Create your views here.

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username,password=raw_password)
			login(request,user)
			return redirect('index')
	else:
		form = SignUpForm()
	return render(request,'signup.html',{'form':form})

def form(request):
	context = locals()
	template = "include/form.html"
	return render(request,template,context)