# Generated by Django 3.2.7 on 2023-07-11 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20230711_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='foryou',
            field=models.ManyToManyField(blank=True, related_name='for_you', to='main.Foryou'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=400)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.blog')),
            ],
        ),
    ]
