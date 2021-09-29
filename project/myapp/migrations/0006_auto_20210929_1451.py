# Generated by Django 3.2.6 on 2021-09-29 09:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210929_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='full_name',
        ),
        migrations.AddField(
            model_name='customuser',
            name='fullname',
            field=models.CharField(default=django.utils.timezone.now, max_length=150, verbose_name='full name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.CharField(max_length=150, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profession',
            field=models.CharField(max_length=150, verbose_name='profession'),
        ),
    ]