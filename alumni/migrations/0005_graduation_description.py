# Generated by Django 3.1.7 on 2021-03-26 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0004_auto_20210326_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='graduation',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
