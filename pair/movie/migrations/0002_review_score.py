# Generated by Django 3.2.13 on 2022-09-30 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='score',
            field=models.CharField(max_length=5, null=True),
        ),
    ]