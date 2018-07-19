# Generated by Django 2.0.6 on 2018-07-18 17:50

from django.db import migrations, models
import trails.validators


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0010_auto_20180620_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trail',
            name='about',
            field=models.TextField(verbose_name='Description of the trail'),
        ),
        migrations.AlterField(
            model_name='trail',
            name='difficulty',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Moderate', 'Moderate'), ('Hard', 'Hard'), ('Extreme', 'Extreme')], max_length=10),
        ),
        migrations.AlterField(
            model_name='trail',
            name='distance',
            field=models.PositiveIntegerField(default='0', verbose_name='Distance (in KM)'),
        ),
        migrations.AlterField(
            model_name='trail',
            name='track',
            field=models.FileField(default='tracklink.kml', upload_to='tracks/', validators=[trails.validators.validate_file_extension], verbose_name='Track (KML file only)'),
        ),
    ]
