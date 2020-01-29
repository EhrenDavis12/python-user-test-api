# Generated by Django 3.0.2 on 2020-01-29 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('last_login', models.DateField()),
                ('login_count', models.IntegerField()),
                ('project_count', models.IntegerField()),
            ],
        ),
    ]
