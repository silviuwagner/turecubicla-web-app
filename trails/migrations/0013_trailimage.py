# Generated by Django 2.2.1 on 2019-06-12 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0012_auto_20180719_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrailImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='image/', verbose_name='image')),
                ('trail', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='trails.Trail')),
            ],
        ),
    ]
