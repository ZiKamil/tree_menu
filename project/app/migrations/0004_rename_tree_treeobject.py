# Generated by Django 4.1.5 on 2023-01-11 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_tree_inheritance'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tree',
            new_name='TreeObject',
        ),
    ]
