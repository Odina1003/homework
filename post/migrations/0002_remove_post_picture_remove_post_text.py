# Generated by Django 4.2.7 on 2023-11-16 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
    ]