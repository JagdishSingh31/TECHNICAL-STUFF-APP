# Generated by Django 3.1.2 on 2020-10-12 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Search',
            new_name='new_search',
        ),
        migrations.AlterModelOptions(
            name='new_search',
            options={'verbose_name_plural': 'Searches'},
        ),
    ]
