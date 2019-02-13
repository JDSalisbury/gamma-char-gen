# Generated by Django 2.1.5 on 2019-02-13 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=25)),
                ('ability', models.CharField(max_length=5)),
                ('skill', models.CharField(max_length=10)),
                ('bonus', models.CharField(max_length=10)),
                ('ac', models.IntegerField()),
                ('fort', models.IntegerField()),
                ('ref', models.IntegerField()),
                ('will', models.IntegerField()),
                ('lvl', models.TextField(max_length=1000)),
                ('lvl_1', models.TextField(max_length=1000)),
                ('lvl_2_or_6', models.TextField(max_length=1000)),
                ('novice', models.TextField(max_length=1000)),
                ('utility', models.TextField(max_length=1000)),
                ('expert', models.TextField(max_length=1000)),
            ],
        ),
    ]
