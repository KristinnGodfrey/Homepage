# Generated by Django 3.1.2 on 2020-10-25 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0005_auto_20201025_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]