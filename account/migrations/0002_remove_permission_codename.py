# Generated by Django 5.0.3 on 2024-03-26 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='codename',
        ),
    ]
