# Generated by Django 5.0.7 on 2024-08-15 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_avatar_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(upload_to='avatares/'),
        ),
    ]
