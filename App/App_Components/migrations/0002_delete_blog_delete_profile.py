# Generated by Django 4.2.2 on 2023-06-20 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Components', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
