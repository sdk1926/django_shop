# Generated by Django 3.2 on 2021-04-26 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0002_fcuser_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='비밀번호'),
        ),
    ]
