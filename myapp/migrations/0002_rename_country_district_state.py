# Generated by Django 4.1.2 on 2022-10-22 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='district',
            old_name='country',
            new_name='State',
        ),
    ]