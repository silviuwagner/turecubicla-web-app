# Generated by Django 2.0.6 on 2018-06-06 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='location',
            field=models.TextField(default='Romania'),
        ),
    ]