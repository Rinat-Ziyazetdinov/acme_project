# Generated by Django 5.2.1 on 2025-06-03 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0002_alter_birthday_birthday'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='birthday',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name', 'birthday'), name='Unique person constraint'),
        ),
    ]
