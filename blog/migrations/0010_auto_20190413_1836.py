# Generated by Django 2.2 on 2019-04-13 18:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20181125_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]