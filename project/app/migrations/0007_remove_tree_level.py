# Generated by Django 4.1.5 on 2023-01-11 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_tree_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tree',
            name='level',
        ),
    ]
