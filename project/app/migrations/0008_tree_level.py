# Generated by Django 4.1.5 on 2023-01-11 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_tree_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]
