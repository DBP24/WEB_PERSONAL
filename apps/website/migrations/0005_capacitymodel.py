# Generated by Django 5.1.3 on 2024-12-19 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_studymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CapacityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ie', models.CharField(max_length=150)),
                ('tema', models.CharField(max_length=150)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('tiempo', models.TimeField()),
            ],
        ),
    ]
