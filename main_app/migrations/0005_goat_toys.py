# Generated by Django 4.1.3 on 2022-11-18 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_toy'),
    ]

    operations = [
        migrations.AddField(
            model_name='goat',
            name='toys',
            field=models.ManyToManyField(to='main_app.toy'),
        ),
    ]
