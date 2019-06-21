from django.urls import path
from Admin import views as Admin_views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
 	path('signup/',Admin_views.signup,name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),

   ]