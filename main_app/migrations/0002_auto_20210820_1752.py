# Generated by Django 3.2.6 on 2021-08-20 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='image',
            new_name='image_url',
        ),
        migrations.AddField(
            model_name='cat',
            name='pending',
            field=models.BooleanField(default=True),
        ),
    ]