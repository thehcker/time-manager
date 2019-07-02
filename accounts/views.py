from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from music.models import Profile
from accounts.forms import ProfileForm

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

@login_required
def userProfile(request):
    user = Profile.objects.new_or_get(request)
    title = Profile.objects.all()
    #profile = request.user.profile
    context = {"title":title, "user": user}
    template = 'profile.html'
    return render(request,template,context)

def model_profile_upload(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'model_profile_upload.html', {
        'form': form
    })
