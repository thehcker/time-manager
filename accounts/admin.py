from django.contrib.auth.admin  import UserAdmin as BaseUserAdmin
from django.contrib import admin
from accounts.models import User

# Register your models here.
class UserAdmin(BaseUserAdmin):
	class Meta:
		model = User
admin.site.register(User, UserAdmin)