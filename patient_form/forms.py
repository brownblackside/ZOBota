from django.forms import ModelForm
from patient_form. models import Form

class FormForm(ModelForm):
    class Meta:
        model = Form
        fields = ['patient_name', 'patient_age', 'patient_gender', 'microcalcinates', 'comment_1', 'solidity', 'echogenicity', 'comment_2', 'contours', 'comment_3', 'bloodflow_1', 'bloodflow_2', 'verticalization', 'histology', 'form_date']
