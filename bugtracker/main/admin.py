
from django.contrib import admin
from .models import Register_Users


@admin.register(Register_Users)
class Register_UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'last_login')