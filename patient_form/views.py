from django.shortcuts import render
from django.db import models
from .models import Form
from django.template import loader
from django.http import HttpResponse
from django.forms import modelformset_factory

#def form(request):
    #return render(request, 'patient_form/form.html')

from .forms import FormForm

def patient_form(request):

    if request.method == 'POST':
        form = FormForm(request.POST)
        if form.is_valid():

            f = form.save()
            hist = Form.objects.filter(patient_name = f.patient_name)
            if f.histology == '1':
                hist.update(result_hist = 'Злокачественное новообразование')
            else:
                hist.update(result_hist = 'Доброкачественное новообразование')
            #Form.objects.filter(patient_name = f.patient_name).update(result_hist = f.histology)

            forms = Form.objects.all()


            return render(request, 'db.html', {'forms': forms})

    else:
        form_class = FormForm

    return render(request, 'form_t.html', {
        'form': form_class,
    })
