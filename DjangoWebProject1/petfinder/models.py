from django.db import models
from passlib.hash import django_pbkdf2_sha256
# Create your models here.

class Usuarios(models.Model):
    nome = models.CharField(max_length = 100, null = False, blank = False)
    email = models.EmailField(null = False, blank = False)
    password = models.CharField(max_length = 256, null = False, blank = False)

    def verify_password(self, raw_password):
        return django_pbkdf2_sha256.verify(raw_password, self.password)