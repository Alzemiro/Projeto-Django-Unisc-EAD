from django.db import models
from passlib.hash import django_pbkdf2_sha256
# Create your models here.

class Usuarios(models.Model):
    nome = models.CharField(max_length = 200, null = False, blank = False)
    email = models.EmailField(null = False, blank = False)
    password = models.CharField(max_length = 256, null = False, blank = False)

    def verify_password(self, raw_password):
        return django_pbkdf2_sha256.verify(raw_password, self.password)

class Animais(models.Model):
    nome = models.CharField(max_length = 200, null = False, blank = False)
    raca = models.CharField(max_length = 45, null = False, blank = False)
    idade = models.IntegerField(null = False, blank = False)
    descricao = models.TextField(null = False, blank = False)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)


class UsuarioAnimal(models.Model):

    ADOCAO_STATUS = (
        ('0', 'Não adotado'),
        ('1', 'Aguardando confirmação de adoção' ),
        ('2', 'Adotado')
        )

    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    id_animal = models.ForeignKey(Animais, on_delete=models.CASCADE)
    status_adocao = models.SmallIntegerField(choices=ADOCAO_STATUS, blank=False, null = False)