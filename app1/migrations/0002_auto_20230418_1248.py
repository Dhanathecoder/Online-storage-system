# Generated by Django 2.0.7 on 2023-04-18 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='file_upload',
            fields=[
                ('ids', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=255)),
                ('my_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
