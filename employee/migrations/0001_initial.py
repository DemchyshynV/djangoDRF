# Generated by Django 3.1.4 on 2021-01-05 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=30)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='office.officemodel')),
            ],
            options={
                'db_table': 'employees',
            },
        ),
    ]