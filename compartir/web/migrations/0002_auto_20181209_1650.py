# Generated by Django 2.1.3 on 2018-12-09 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('author', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Category'),
        ),
    ]
