# Generated by Django 2.2.6 on 2019-10-30 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_auto_20191030_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinfo',
            name='userid',
            field=models.IntegerField(default=None),
        ),
    ]
