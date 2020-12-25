# Generated by Django 3.1.4 on 2020-12-24 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'office',
            },
        ),
    ]
