# Generated by Django 2.2.7 on 2019-11-20 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_blog_update_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='update_at',
            field=models.TextField(blank=True),
        ),
    ]
