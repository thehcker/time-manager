from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from .forms import ManagerSignUpForm
from accounts.models import User
# Create your views here.

def manager_signup(request):
	if request.method == 'POST':
		form = ManagerSignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username,password=raw_password)
			login(request,user)
			return redirect('index')
	else:
		form = ManagerSignUpForm()
	return render(request,'manager_signup.html',{'form':form})


def manage_users(request):
	all_users = User.objects.all()
	template = 'includes/all_users.html'
	return render(request, template, {'all_users': all_users})