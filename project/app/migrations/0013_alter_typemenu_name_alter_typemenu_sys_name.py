# Generated by Django 4.1.5 on 2023-01-12 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_typemenu_sys_name_alter_typemenu_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typemenu',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='typemenu',
            name='sys_name',
            field=models.CharField(max_length=200),
        ),
    ]
