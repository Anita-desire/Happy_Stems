# Generated by Django 4.0.5 on 2022-06-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='users1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=600)),
                ('PhoneNo', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='users',
        ),
    ]
