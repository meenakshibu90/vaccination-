import django_filters
from django import forms
from django_filters import CharFilter
from .models import Hospital


class HospitalFilter(django_filters.FilterSet):
    name=CharFilter(field_name='name',label="",lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder':'Search Name','class':'form-control'}))

    class Meta:
        model=Hospital
        fields=('name',)




