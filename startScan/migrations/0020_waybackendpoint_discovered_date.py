# Generated by Django 3.1.3 on 2020-11-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0019_auto_20201126_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='waybackendpoint',
            name='discovered_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
