# Generated by Django 3.1.2 on 2020-10-27 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20201026_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='status',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
