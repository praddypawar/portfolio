# Generated by Django 4.0.5 on 2022-11-10 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_folioviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(default='system', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='system', max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.PositiveIntegerField(choices=[(0, 'inactive'), (1, 'active'), (2, 'deleted_by_owner')], default=1)),
                ('designation', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('start_data', models.DateField()),
                ('end_data', models.DateField(blank=True, null=True)),
                ('description', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.basicinfo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
