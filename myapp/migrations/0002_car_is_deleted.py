# Generated by Django 2.0.4 on 2018-05-01 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
