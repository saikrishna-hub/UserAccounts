# Generated by Django 2.2.6 on 2019-10-26 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_auto_20191017_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]