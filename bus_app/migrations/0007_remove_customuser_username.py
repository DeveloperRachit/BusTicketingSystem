# Generated by Django 4.2.8 on 2024-01-05 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bus_app', '0006_customuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
