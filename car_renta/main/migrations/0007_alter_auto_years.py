# Generated by Django 4.0.5 on 2022-06-23 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='years',
            field=models.ImageField(max_length=20, upload_to=''),
        ),
    ]