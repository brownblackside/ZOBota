from django.shortcuts import render
from django.db import models
from .models import Form
from django.template import loader
from django.http import HttpResponse
from django.forms import modelformset_factory
from .neuron import NeuralNetwork
from numpy import exp, array, dot, random

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
            
            neuro = Form.objects.filter(patient_name = f.patient_name)
            input_usi = [f.microcalcinates, f.solidity, f.echogenicity, f.contours, f.bloodflow_1, f.bloodflow_2, f.verticalization]

            neural_network = NeuralNetwork()

            training_set_inputs = array([[0, 0, 0, 0, 1, 1, 0],
                                         [0, 0, 0, 0, 0, 1, 0],
                                         [0, 1, 1, 0, 0, 0, 0],
                                         [0, 1, 1, 0, 1, 1, 0],
                                         [1, 1, 1, 1, 1, 1, 0],
                                         [1, 1, 1, 1, 0, 1, 0],
                                         [1, 1, 1, 1, 0, 1, 0],
                                         [1, 1, 0, 0, 0, 0, 0],
                                         [1, 1,	1, 1, 1, 1,	0],
                                         [1, 1, 1, 1, 1, 1,	1],
                                         [1, 1,	1, 1, 0, 1,	1],
                                         [0, 1,	0, 0, 1, 1,	0],
                                         [1, 1,	0, 0, 1, 1,	0],
                                         [1, 1,	1 ,1, 0, 1,	1],
                                         [0, 1,	1, 0, 0, 0,	0],
                                         [1, 1,	1, 1, 1, 1,	0],
                                         [0, 0,	0, 0, 0, 1,	0],
                                         [0, 1,	0, 1, 0, 1,	0],
                                         [0, 0, 0, 0, 0, 1, 0],
                                         [1, 1,	1, 1, 0, 1, 1],
                                         [0, 0,	1, 0, 0, 1,	0],
                                         [1, 1,	1, 1, 1, 1,	1],
                                         [1, 1,	0, 1, 1, 1,	1],
                                         [1, 0, 0, 1, 0, 0,	0],
                                         [1, 1,	1, 1, 0, 1,	0],
                                         [1, 0,	0, 0, 0, 1,	1],
                                         [0, 0,	0, 0, 1, 1,	0],
                                         [0, 0,	0, 0, 0, 1,	0],
                                         [0, 0,	0, 0, 1, 1,	0],
                                         [0, 0,	0, 0, 0, 1,	0],
                                         [1, 1,	0, 1, 0, 0,	1],
                                         [0, 1,	1, 0, 1, 1,	0],
                                         [1, 1, 0, 1, 1, 1,	1],
                                         ])


            training_set_outputs = array([[0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1]]).T

            neural_network.train(training_set_inputs, training_set_outputs, 20000)

            usi_input = input_usi

            for i in range(len(usi_input)):
                usi_input[i] = int(usi_input[i])

            result = neural_network.think(array(usi_input)).tolist()
            r_result = result[0]

            if r_result >= 0.5:
                neuro.update(result_neuro = 'Злокачественное новообразование')
            else:
                neuro.update(result_neuro = 'Доброкачественное новообразование')

            forms = Form.objects.all()


            return render(request, 'db.html', {'forms': forms})

    else:
        form_class = FormForm

    return render(request, 'form_t.html', {
        'form': form_class,
    })
