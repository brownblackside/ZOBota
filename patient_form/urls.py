from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('form_t/', views.patient_form),
    path('db/', views.patient_form),

path('', admin.site.urls)
]
