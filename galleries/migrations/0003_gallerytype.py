# Generated by Django 3.1.4 on 2021-01-04 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0002_auto_20201228_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='gallerytype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'verbose_name': 'gallery_types',
            },
        ),
    ]