# Generated by Django 5.1.3 on 2024-12-31 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_studymodel_url_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='')),
                ('urls', models.TextField(max_length=250, verbose_name='')),
                ('description', models.TextField(max_length=500, verbose_name='')),
                ('photo', models.ImageField(blank=True, default='static/images/default.jpg', null=True, upload_to='static/images/', verbose_name='foto')),
            ],
        ),
    ]
