# Generated by Django 4.0.5 on 2022-06-23 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='if_email_verified',
            field=models.BooleanField(default=False),
        ),
    ]
