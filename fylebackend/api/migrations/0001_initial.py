# Generated by Django 3.0.5 on 2021-01-06 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('ifsc', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('bank_id', models.BigIntegerField(null=True)),
                ('branch', models.CharField(max_length=74, null=True)),
                ('address', models.CharField(max_length=195, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('district', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=26, null=True)),
                ('bank_name', models.CharField(max_length=49, null=True)),
            ],
        ),
    ]
