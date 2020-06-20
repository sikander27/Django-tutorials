# Generated by Django 3.0.7 on 2020-06-18 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pease', '0005_auto_20200616_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=30)),
                ('ename', models.CharField(max_length=30)),
                ('eemail', models.EmailField(max_length=254)),
                ('econtact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
