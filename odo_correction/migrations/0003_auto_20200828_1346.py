# Generated by Django 3.1 on 2020-08-28 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odo_correction', '0002_excel_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excel',
            name='file',
            field=models.FileField(upload_to='excel'),
        ),
    ]
