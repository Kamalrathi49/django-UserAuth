# Generated by Django 3.2.6 on 2021-09-29 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20210929_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='fullname',
            new_name='full_name',
        ),
    ]
