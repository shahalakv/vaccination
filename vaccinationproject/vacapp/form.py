import datetime
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from vacapp.models import Vaccination, Hospital, Vaccine, Appointment, Complaint, Book_Appointment, Report_Card
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class UserForm(UserCreationForm):
    username = forms.CharField(max_length=250)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=250)
    class Meta:
        model = Vaccination
        fields = ('username', 'password1', 'password2', 'address', 'child_name', 'child_age', 'gender')


class NurseForm(UserCreationForm):
    username = forms.CharField(max_length=250)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=250)
    class Meta:
        model = Vaccination
        fields = ('username', 'password1', 'password2', 'name', 'email', 'address', 'hospital')


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ('name', 'place', 'email', 'contact')


class VaccineForm(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ('vaccine_name', 'type', 'description')

class TimeInput(forms.TimeInput):
    input_type = 'time'
class AppointmentForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput)
    end_time = forms.TimeField(widget=TimeInput)
    class Meta:
        model = Appointment
        fields = ('hospital', 'date', 'start_time', 'end_time', 'vaccine')
    def clean_date(self):
        date = self.cleaned_data['date']
        if date != datetime.date.today():
            raise forms.ValidationError("Invalid Date")
        return date

class ComplaintForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)

    class Meta:
        model = Complaint
        fields = ('user', 'subject', 'complaint', 'date')

    def clean_date(self):
        date = self.cleaned_data['date']
        if date != datetime.date.today():
            raise forms.ValidationError("Invalid Date")
        return date


class Book_AppointmentForm(forms.ModelForm):
    class Meta:
        model = Book_Appointment
        fields = ('user', 'schedule', 'vaccine_name', 'vaccinated', 'status')


class Report_CardForm(forms.ModelForm):
    class Meta:
        model = Report_Card
        fields = ('user', 'child_age', 'date', 'vaccine')
