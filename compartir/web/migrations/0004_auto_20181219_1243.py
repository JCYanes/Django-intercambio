# Generated by Django 2.1.3 on 2018-12-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20181209_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
