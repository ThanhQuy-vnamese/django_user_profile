# Generated by Django 3.2.4 on 2021-06-21 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userlist', '0002_auto_20210621_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
