# Generated by Django 3.0a1 on 2019-10-24 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20190928_0435'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='ads',
            field=models.CharField(default=1, max_length=100, verbose_name='Phone'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='fn',
            field=models.CharField(default=1, max_length=100, verbose_name='First name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='ln',
            field=models.CharField(default=1, max_length=100, verbose_name='Last name'),
            preserve_default=False,
        ),
    ]