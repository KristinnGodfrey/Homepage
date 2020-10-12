# Generated by Django 3.1.2 on 2020-10-12 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100)),
                ('type', models.IntegerField(choices=[(1, 'Webdev'), (2, 'Software'), (3, 'Database')])),
            ],
        ),
    ]
