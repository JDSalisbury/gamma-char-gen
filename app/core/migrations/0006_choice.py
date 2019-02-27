# Generated by Django 2.1.5 on 2019-02-17 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_originsecondary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_primary', models.OneToOneField(on_delete='', to='core.Origin')),
                ('o_secondary', models.OneToOneField(on_delete='', to='core.OriginSecondary')),
            ],
        ),
    ]