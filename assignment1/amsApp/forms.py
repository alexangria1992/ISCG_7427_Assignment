
from django.forms import ModelForm
from django import forms
from .models import Child,Activity
from assignment1 import settings


class DateInput(forms.DateInput):
    input_type = 'date'
   


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'
    
class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        
        fields = ['name','date','start_time','duration']
        
        widgets = {
           'start_time' : forms.TimeInput(),
           'date' : DateInput(),
           
        }


class ChildForm(ModelForm):
     class Meta:
        model = Child
        
        fields = ['name','date_of_birth','address','contact']
        
        widgets = {
            'date_of_birth': DateInput(),
        }
