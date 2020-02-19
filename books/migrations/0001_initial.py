# Generated by Django 3.0.3 on 2020-02-17 11:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('isbn', models.CharField(max_length=50)),
                ('authors', models.CharField(max_length=1000)),
                ('number_of_pages', models.PositiveIntegerField(default=0)),
                ('publisher', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('release_date', models.DateField()),
            ],
        ),
    ]
