# Generated by Django 4.0.2 on 2022-11-02 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('animal', models.CharField(max_length=500)),
                ('quantity', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
    ]
