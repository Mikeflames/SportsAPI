# Generated by Django 4.0.5 on 2022-06-06 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0002_sports_teacher_sports_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='sports',
            new_name='sports_player',
        ),
    ]