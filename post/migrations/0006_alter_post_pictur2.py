# Generated by Django 4.2.7 on 2023-11-16 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_post_avatar_post_pictur2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pictur2',
            field=models.ImageField(blank=True, null=True, upload_to='post/static/images/'),
        ),
    ]