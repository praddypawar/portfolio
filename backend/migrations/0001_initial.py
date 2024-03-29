# Generated by Django 4.0.5 on 2022-11-08 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(default='system', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='system', max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.PositiveIntegerField(choices=[(0, 'inactive'), (1, 'active'), (2, 'deleted_by_owner')], default=1)),
                ('uname', models.CharField(max_length=50, unique=True)),
                ('fname', models.CharField(max_length=50)),
                ('mname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender')], max_length=1)),
                ('profile', models.ImageField(upload_to='')),
                ('dob', models.DateField()),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
