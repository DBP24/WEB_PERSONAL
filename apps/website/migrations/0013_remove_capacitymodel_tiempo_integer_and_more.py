# Generated by Django 5.1.3 on 2025-02-25 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_remove_capacitymodel_tiempo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capacitymodel',
            name='tiempo_integer',
        ),
        migrations.AddField(
            model_name='capacitymodel',
            name='tiempo_entero',
            field=models.IntegerField(default=0),
        ),
    ]
