# Generated by Django 3.2.6 on 2021-09-05 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='authorAvatar',
            field=models.ImageField(default=None, height_field='100', upload_to='', width_field='100%'),
        ),
    ]
