# Generated by Django 2.2.1 on 2019-09-18 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190919_0335'),
    ]

    operations = [
        migrations.CreateModel(
            name='aboutTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='About Title')),
            ],
        ),
        migrations.CreateModel(
            name='contactTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Contact Title')),
            ],
        ),
        migrations.CreateModel(
            name='portfolioTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Portfolio Title')),
            ],
        ),
        migrations.CreateModel(
            name='serviceTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Service Title')),
            ],
        ),
        migrations.CreateModel(
            name='testimonialTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Testimonial Title')),
            ],
        ),
    ]
