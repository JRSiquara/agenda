# Generated by Django 3.2.9 on 2021-11-16 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20211112_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='local',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]