# Generated by Django 3.0.8 on 2020-07-25 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_form', '0004_auto_20200724_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='result_hist',
            field=models.CharField(default='', max_length=30, verbose_name='Гистологическое заключение'),
        ),
        migrations.AlterField(
            model_name='form',
            name='result',
            field=models.CharField(default='', max_length=30, verbose_name='Заключение Нейросети'),
        ),
    ]
