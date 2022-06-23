# Generated by Django 4.0.5 on 2022-06-23 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_auto_years'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='model',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='main.auto'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='years',
            field=models.IntegerField(),
        ),
    ]