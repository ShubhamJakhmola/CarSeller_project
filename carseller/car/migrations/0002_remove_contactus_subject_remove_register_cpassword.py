# Generated by Django 4.1.2 on 2022-10-20 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='register',
            name='cpassword',
        ),
    ]
