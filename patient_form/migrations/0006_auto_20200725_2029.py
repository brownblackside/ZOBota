# Generated by Django 3.0.8 on 2020-07-25 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient_form', '0005_auto_20200725_2027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='result',
            new_name='result_neuro',
        ),
    ]