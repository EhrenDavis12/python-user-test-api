# Generated by Django 3.0.2 on 2020-02-02 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_auto_20200128_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]