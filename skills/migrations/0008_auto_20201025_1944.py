# Generated by Django 3.1.2 on 2020-10-25 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0007_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateField(verbose_name='date of project'),
        ),
    ]
