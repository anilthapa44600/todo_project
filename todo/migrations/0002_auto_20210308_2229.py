# Generated by Django 3.1.7 on 2021-03-08 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.CharField(default='normal', max_length=10),
        ),
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.CharField(default='0', max_length=1),
        ),
    ]