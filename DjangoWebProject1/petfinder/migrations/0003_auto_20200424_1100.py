# Generated by Django 3.0.5 on 2020-04-24 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petfinder', '0002_auto_20200424_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarioanimal',
            name='status_adocao',
            field=models.SmallIntegerField(choices=[('0', 'Não adotado'), ('1', 'Aguardando confirmação de adoção'), ('2', 'Adotado')]),
        ),
    ]