# Generated by Django 4.1.1 on 2022-10-01 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar_app', '0006_pitch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitch',
            name='load_capacity',
            field=models.CharField(default='', max_length=50),
        ),
    ]
