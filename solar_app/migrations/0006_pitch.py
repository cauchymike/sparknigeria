# Generated by Django 4.1.1 on 2022-10-01 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar_app', '0005_dashboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pitch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=45, null=True)),
                ('lastname', models.CharField(max_length=45, null=True)),
                ('emailaddress', models.CharField(max_length=45, null=True, unique=True)),
                ('phonenumber', models.CharField(max_length=45, null=True)),
                ('city', models.CharField(max_length=45, null=True)),
                ('no_of_users', models.DecimalField(decimal_places=2, default=0, max_digits=16)),
                ('load_capacity', models.DecimalField(decimal_places=2, default=0, max_digits=16)),
                ('extra_details', models.CharField(default='', max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created_at')),
            ],
        ),
    ]
