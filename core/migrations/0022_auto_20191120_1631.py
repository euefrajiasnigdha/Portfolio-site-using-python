# Generated by Django 2.2.7 on 2019-11-20 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20191120_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='update_at',
            field=models.TextField(blank=True, null=True),
        ),
    ]
