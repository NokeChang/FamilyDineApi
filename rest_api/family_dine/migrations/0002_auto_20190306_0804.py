# Generated by Django 2.1.7 on 2019-03-06 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family_dine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dine',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dine_opened', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='dine',
            name='participant',
            field=models.ManyToManyField(blank=True, related_name='dine_joined', to=settings.AUTH_USER_MODEL),
        ),
    ]