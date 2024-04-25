from django.contrib.auth.hashers import make_password
from django.db import models


# Create your models here.

class Register_Users(models.Model):
    username = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    password = models.CharField(max_length=128, blank=False, null=False)
    last_login = models.DateTimeField(auto_now=True, verbose_name='Last Login')

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)  # Хеширование пароля перед сохранением
        super(Register_Users, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Список пользователей'
