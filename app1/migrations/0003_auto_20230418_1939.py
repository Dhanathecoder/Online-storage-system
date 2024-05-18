# Generated by Django 2.0.7 on 2023-04-18 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20230418_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='files/%y')),
                ('file_name', models.CharField(max_length=255)),
                ('file_file', models.FileField(upload_to='files/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='file_upload',
        ),
    ]