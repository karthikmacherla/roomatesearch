# Generated by Django 2.2 on 2019-05-07 05:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190506_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
