# Generated by Django 5.0.7 on 2024-08-15 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSamuel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='libros/'),
        ),
    ]
