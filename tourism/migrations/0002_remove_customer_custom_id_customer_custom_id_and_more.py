# Generated by Django 4.0 on 2022-01-01 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='custom_ID',
        ),
        migrations.AddField(
            model_name='customer',
            name='custom_id',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='customer',
            name='url',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]