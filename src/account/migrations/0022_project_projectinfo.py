# Generated by Django 2.2.6 on 2019-10-30 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_kycinfo_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(max_length=50)),
                ('projectcode', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectcode', models.CharField(default=None, max_length=100, null=True)),
                ('projectname', models.CharField(default=None, max_length=100)),
                ('userid', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('minprice', models.IntegerField(default=None)),
                ('maxprice', models.IntegerField(default=None)),
            ],
        ),
    ]