# Generated by Django 4.2.7 on 2023-11-19 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transitXpress', '0004_conformation_from_location_conformation_to_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conformation',
            name='from_location',
            field=models.CharField(default='Default From Location', max_length=255, null=True),
        ),
    ]
