# Generated by Django 2.2.6 on 2019-10-29 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20191029_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='kycinfo',
            name='idproofback',
            field=models.BinaryField(default=None),
        ),
        migrations.AddField(
            model_name='kycinfo',
            name='idprooffront',
            field=models.BinaryField(default=None),
        ),
    ]