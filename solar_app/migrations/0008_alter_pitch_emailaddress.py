# Generated by Django 4.1.1 on 2022-10-01 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar_app', '0007_alter_pitch_load_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitch',
            name='emailaddress',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
