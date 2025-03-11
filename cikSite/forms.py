from django.forms import ModelForm, TextInput, NumberInput, DateTimeInput
from .models import Voting
from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()


class VotingForm(ModelForm):
    class Meta:
        model = Voting
        fields = ['title', 'number_kand', 'number_izb', 'time', 'email']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название выборов'
            }),
            'number_kand': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Кол-во кандидатов'
            }),
            'number_izb': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Кол-во избирателей'
            }),
            'time': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время',
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта'
            })

        }