# Generated by Django 5.0.6 on 2024-06-06 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_socialuser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialuser',
            name='first_name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='socialuser',
            name='last_name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
