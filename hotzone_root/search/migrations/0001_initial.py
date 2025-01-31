# Generated by Django 3.1.2 on 2020-10-31 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addressZH', models.CharField(max_length=200)),
                ('nameZH', models.CharField(max_length=200)),
                ('x', models.DecimalField(decimal_places=0, max_digits=20)),
                ('y', models.DecimalField(decimal_places=0, max_digits=20)),
                ('nameEN', models.CharField(max_length=200)),
                ('addressEN', models.CharField(max_length=200)),
            ],
        ),
    ]
