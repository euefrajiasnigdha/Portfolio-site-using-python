# Generated by Django 2.2.1 on 2019-09-19 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20190920_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideimage',
            name='image',
            field=models.ImageField(upload_to='slideimage'),
        ),
    ]
