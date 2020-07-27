from django.db import models
import datetime

class Form(models.Model):
    patient_name = models.CharField(max_length = 200, verbose_name = 'ФИО')
    patient_age = models.CharField(max_length = 30, verbose_name = 'Возраст')
    gender_choice = [
        ('женский', 'женский'),
        ('мужской', 'мужской')
        ]
    patient_gender = models.CharField(max_length = 30, choices = gender_choice, default = 'женский', verbose_name = 'Пол')
    microcalcinates = models.CharField(max_length = 30, verbose_name = 'Микрокальцинаты')
    comment_1 = models.CharField(max_length = 200, verbose_name = 'Комментарий')
    solidity = models.CharField(max_length = 30, verbose_name = 'Солидность')
    echogenicity = models.CharField(max_length = 30, verbose_name = 'Эхогенность')
    comment_2 = models.CharField(max_length = 200, verbose_name = 'Комментарий')
    contours = models.CharField(max_length = 30, verbose_name = 'Контуры')
    comment_3 = models.CharField(max_length = 200, verbose_name = 'Комментарий')
    bloodflow_1 = models.CharField(max_length = 30, verbose_name = 'Кровоток 1')
    bloodflow_2 = models.CharField(max_length = 30, verbose_name = 'Кровоток 2')
    verticalization = models.CharField(max_length = 30, verbose_name = 'Вертикализация')
    histology = models.CharField(max_length = 30, verbose_name = 'Гистология', default = '')
    form_date = models.DateField(default=datetime.date.today, verbose_name = 'Дата')
    result_neuro = models.CharField(max_length = 30, verbose_name = 'Заключение Нейросети', default = '')
    result_hist = models.CharField(max_length = 30, verbose_name = 'Гистологическое заключение', default = '')

    def __str__(self):
        return self.patient_name
