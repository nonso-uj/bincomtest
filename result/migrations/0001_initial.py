# Generated by Django 4.1 on 2022-08-16 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnouncedPuResults',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('polling_unit_uniqueid', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'announced_pu_results',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AnnouncedLgaResults',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('lga_name', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'announced_lga_results',
            },
        ),
        migrations.CreateModel(
            name='AnnouncedStateResults',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'announced_state_results',
            },
        ),
        migrations.CreateModel(
            name='AnnouncedWardResults',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('ward_name', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'announced_ward_results',
            },
        ),
    ]