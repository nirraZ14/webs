# Generated by Django 3.2.7 on 2023-07-11 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_service_foryou'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='description',
        ),
        migrations.RemoveField(
            model_name='service',
            name='foryou',
        ),
        migrations.AddField(
            model_name='service',
            name='foryou',
            field=models.ManyToManyField(default=True, to='main.Foryou'),
        ),
    ]
