# Generated by Django 3.0.8 on 2020-07-21 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=200)),
                ('patient_age', models.CharField(max_length=30)),
                ('microcalcinates', models.CharField(max_length=30)),
                ('comment_1', models.CharField(max_length=200)),
                ('solidity', models.CharField(max_length=30)),
                ('echogenicity', models.CharField(max_length=30)),
                ('comment_2', models.CharField(max_length=200)),
                ('contours', models.CharField(max_length=30)),
                ('comment_3', models.CharField(max_length=200)),
                ('bloodflow_1', models.CharField(max_length=30)),
                ('bloodflow_2', models.CharField(max_length=30)),
                ('verticalization', models.CharField(max_length=30)),
                ('histology', models.CharField(max_length=30)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
