# Generated by Django 3.1 on 2020-08-28 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odo_correction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='excel',
            name='country',
            field=models.CharField(default='', max_length=20),
        ),
    ]
