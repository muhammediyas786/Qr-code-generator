# Generated by Django 4.1.5 on 2023-01-16 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_qr_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qr',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
