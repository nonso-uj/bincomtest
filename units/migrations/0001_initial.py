# Generated by Django 4.1 on 2022-08-18 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agentname',
            fields=[
                ('name_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(max_length=13)),
                ('pollingunit_uniqueid', models.IntegerField()),
            ],
            options={
                'db_table': 'agentname',
            },
        ),
        migrations.CreateModel(
            name='Lga',
            fields=[
                ('uniqueid', models.AutoField(primary_key=True, serialize=False)),
                ('lga_id', models.IntegerField()),
                ('lga_name', models.CharField(max_length=50)),
                ('state_id', models.IntegerField()),
                ('lga_description', models.TextField(blank=True, null=True)),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'lga',
            },
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partyid', models.CharField(max_length=11)),
                ('partyname', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'party',
            },
        ),
        migrations.CreateModel(
            name='PollingUnit',
            fields=[
                ('uniqueid', models.AutoField(primary_key=True, serialize=False)),
                ('polling_unit_id', models.IntegerField()),
                ('ward_id', models.IntegerField()),
                ('lga_id', models.IntegerField()),
                ('uniquewardid', models.IntegerField(blank=True, null=True)),
                ('polling_unit_number', models.CharField(blank=True, max_length=50, null=True)),
                ('polling_unit_name', models.CharField(blank=True, max_length=50, null=True)),
                ('polling_unit_description', models.TextField(blank=True, null=True)),
                ('lat', models.CharField(blank=True, max_length=255, null=True)),
                ('long', models.CharField(blank=True, max_length=255, null=True)),
                ('entered_by_user', models.CharField(blank=True, max_length=50, null=True)),
                ('date_entered', models.DateTimeField(blank=True, null=True)),
                ('user_ip_address', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'polling_unit',
            },
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('state_id', models.IntegerField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'states',
            },
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('uniqueid', models.AutoField(primary_key=True, serialize=False)),
                ('ward_id', models.IntegerField()),
                ('ward_name', models.CharField(max_length=50)),
                ('lga_id', models.IntegerField()),
                ('ward_description', models.TextField(blank=True, null=True)),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'ward',
            },
        ),
    ]
