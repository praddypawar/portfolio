# Generated by Django 4.0.5 on 2022-11-10 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_alter_workexperience_end_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='end_data',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]