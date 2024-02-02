from django import forms
from django_filters import CharFilter
from vacapp.models import Hospital, Vaccination, Vaccine, Appointment, Complaint, Book_Appointment
import django_filters


class HospitalFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', label="", lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))
    class Meta:
        model = Hospital
        fields = ('name',)

class UserFilter(django_filters.FilterSet):
    name = CharFilter(field_name='username', label="", lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))
    class Meta:
        model = Vaccination
        fields = ('name',)

class NurseFilter(django_filters.FilterSet):
    name = CharFilter(field_name='username', label="", lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))
    class Meta:
        model = Vaccination
        fields = ('name',)


class VaccineFilter(django_filters.FilterSet):
    name = CharFilter(field_name='vaccine_name', label="", lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))
    class Meta:
        model = Vaccine
        fields = ('name',)

class BookFilter(django_filters.FilterSet):
    name = CharFilter(field_name='vaccine_name', label="", lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))
    class Meta:
        model = Appointment
        fields = ('name',)

class ComplaintFilter(django_filters.FilterSet):
    name = CharFilter(field_name='date', label="", lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))
    class Meta:
        model = Complaint
        fields = ('name',)

class VaccinationFilter(django_filters.FilterSet):
    name = CharFilter(field_name='vaccine_name', label="", lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))
    class Meta:
        model = Book_Appointment
        fields = ('name',)

class VaccinesFilter(django_filters.FilterSet):
    name = CharFilter(field_name='vaccine_name', label="", lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))
    class Meta:
        model = Vaccine
        fields = ('name',)

class UsersFilter(django_filters.FilterSet):
    name = CharFilter(field_name='username', label="", lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))
    class Meta:
        model = Vaccination
        fields = ('name',)

class HospitalsFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', label="", lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))
    class Meta:
        model = Hospital
        fields = ('name',)

class SchedulesFilter(django_filters.FilterSet):
    name = CharFilter(field_name='vaccine', label="", lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))
    class Meta:
        model = Appointment
        fields = ('name',)

class ComplaintsFilter(django_filters.FilterSet):
    name = CharFilter(field_name='date', label="", lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))
    class Meta:
        model = Complaint
        fields = ('name',)

class SchedulezFilter(django_filters.FilterSet):
    name = CharFilter(field_name='date', label="", lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))
    class Meta:
        model = Appointment
        fields = ('name',)

# class AppointmentzFilter(django_filters.FilterSet):
#     name = CharFilter(field_name='date', label="", lookup_expr='icontains',widget=forms.TextInput(attrs={
#         'placeholder': 'Search Name', 'class': 'form-control'}))
#     class Meta:
#         model = Appointment
#         fields = ('name',)

class ComplaintzFilter(django_filters.FilterSet):
    name = CharFilter(field_name='date', label="", lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))
    class Meta:
        model = Complaint
        fields = ('name',)

class ReportcardzFilter(django_filters.FilterSet):
    name = CharFilter(field_name='vaccine_name', label="", lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))
    class Meta:
        model = Book_Appointment
        fields = ('name',)




