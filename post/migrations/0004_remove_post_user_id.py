# Generated by Django 3.2.6 on 2021-08-23 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_postimage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user_id',
        ),
    ]