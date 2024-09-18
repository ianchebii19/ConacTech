from django import forms
from . models import *

from django.contrib.auth.forms import UserCreationForm
class NoteForm(forms.Form):
    class Meta:
        model = Note
        fields = ['title', 'description', ]

class DateInput(forms.DateInput):
    input_type = 'date'
        
class HomeworkForm(forms.Form):
    class Meta:
        model = Homework
        widgets = {'due' : DateInput()}
        fields = ['subject', 'title', 'description', 'due', 'is_finished']

class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100, label ="Enter your search")
    

class TodoForm(forms.Form):
    class Meta:
        model = Todo
        fields =['title', 'is_finished', ]

class ConversionForm(forms.Form):
    CHOICES = [('length', 'Length'), ('mass', 'Mass')]
    measurement = forms.ChoiceField( choices=CHOICES, widget=forms.RadioSelect)

class ConversionLengthForm(forms.Form):
       CHOICES = [('yard', 'Yard'), ('foot', 'Foot')]
       input = forms.ChoiceField( required=False, label=False, widget=forms.TextInput(
           attrs ={'type': 'number', 'placehlder':'Enter the Number'}
       ) )
       measurement1 = forms.ChoiceField(
           label='', widget= forms.Select(choice=CHOICES)
       )
       measurement2 = forms.ChoiceField(
           label='', widget= forms.Select(choice=CHOICES)
       )

       
class ConversionMassForm(form.Form):
       CHOICES = [('pound', 'Pound'), ('kilogram', 'Kilogram  ')]
       input = forms.ChoiceField( required=False, label=False, widget=forms.TextInput(
           attrs ={'type': 'number', 'placehlder':'Enter the Number'}
       ) )
       measurement1 = forms.ChoiceField(
           label='', widget= forms.Select(choice=CHOICES)
       )
       measurement2 = forms.ChoiceField(
           label='', widget= forms.Select(choice=CHOICES)
       )


class UserRegistrationForm(UserCreationForm):
     class Meta:
          fields =['username', 'password', 'password2']