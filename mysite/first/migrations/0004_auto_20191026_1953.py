# Generated by Django 2.2.6 on 2019-10-26 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_auto_20191026_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='register',
            name='firstname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='register',
            name='hobbies',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='register',
            name='lastname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='register',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='register',
            name='username',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]
