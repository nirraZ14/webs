# Generated by Django 3.2.7 on 2023-07-11 01:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_foryou_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='foryou',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Foryou',
        ),
    ]
