# Generated by Django 3.2.6 on 2021-08-31 06:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='address'),
            preserve_default=False,
        ),
    ]