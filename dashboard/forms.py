from django import forms
from .models import Note, Homework, Todo  # Import the necessary models
from django.contrib.auth.models import User  # Import User model for registration

from django.contrib.auth.forms import UserCreationForm

class NoteForm(forms.ModelForm):  # Use ModelForm
    class Meta:
        model = Note
        fields = ['title', 'description']

class DateInput(forms.DateInput):
    input_type = 'date'

class HomeworkForm(forms.ModelForm):  # Use ModelForm
    class Meta:
        model = Homework
        widgets = {'due': DateInput()}
        fields = ['subject', 'title', 'description', 'due', 'is_finished']

class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100, label="Enter your search")

class TodoForm(forms.ModelForm):  # Use ModelForm
    class Meta:
        model = Todo
        fields = ['title', 'is_finished']

class ConversionForm(forms.Form):
    CHOICES = [('length', 'Length'), ('mass', 'Mass')]
    measurement = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

class ConversionLengthForm(forms.Form):
    CHOICES = [('yard', 'Yard'), ('foot', 'Foot')]
    input = forms.FloatField(required=False, label=False, widget=forms.TextInput(
        attrs={'type': 'number', 'placeholder': 'Enter the Number'}
    ))
    measurement1 = forms.ChoiceField(choices=CHOICES, label='')
    measurement2 = forms.ChoiceField(choices=CHOICES, label='')

class ConversionMassForm(forms.Form):
    CHOICES = [('pound', 'Pound'), ('kilogram', 'Kilogram')]
    input = forms.FloatField(required=False, label=False, widget=forms.TextInput(
        attrs={'type': 'number', 'placeholder': 'Enter the Number'}
    ))
    measurement1 = forms.ChoiceField(choices=CHOICES, label='')
    measurement2 = forms.ChoiceField(choices=CHOICES, label='')

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User  # Specify the model
        fields = ['username', 'password1', 'password2']  # Use password1 and password2
