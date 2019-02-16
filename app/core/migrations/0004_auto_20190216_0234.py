# Generated by Django 2.1.5 on 2019-02-16 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190213_0336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('origin_primary', models.CharField(max_length=25)),
                ('origin_secondary', models.CharField(max_length=25)),
                ('ability_primary', models.CharField(max_length=5)),
                ('ability_secondary', models.CharField(max_length=5)),
                ('skill_primary', models.CharField(max_length=100)),
                ('skill_secondary', models.CharField(max_length=100)),
                ('bonus_primary', models.CharField(max_length=100)),
                ('bonus_secondary', models.CharField(max_length=100)),
                ('ac', models.IntegerField()),
                ('fort', models.IntegerField()),
                ('ref', models.IntegerField()),
                ('will', models.IntegerField()),
                ('defense_primary', models.TextField(max_length=1000)),
                ('defense_secondary', models.TextField(max_length=1000)),
                ('lvl_1_primary', models.TextField(max_length=1000)),
                ('lvl_1_secondary', models.TextField(max_length=1000)),
                ('lvl_2_or_6_primary', models.TextField(max_length=1000)),
                ('lvl_2_or_6_secondary', models.TextField(max_length=1000)),
                ('novice_primary', models.TextField(max_length=1000)),
                ('novice_secondary', models.TextField(max_length=1000)),
                ('utility_primary', models.TextField(max_length=1000)),
                ('utility_secondary', models.TextField(max_length=1000)),
                ('expert_primary', models.TextField(max_length=1000)),
                ('expert_secondary', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=25)),
                ('key_ability', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='random_skill',
            field=models.OneToOneField(on_delete='', to='core.Skills'),
        ),
    ]
