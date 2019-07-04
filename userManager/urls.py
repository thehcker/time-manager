from django.urls import path
from userManager import views as userManager_views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
 	path('manager_signup/',userManager_views.manager_signup,name='manager_signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),

   ]