# from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm
from django import forms

# class TestSignupForm(forms.ModelForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['first_name', 'last_name',]
#
#     def signup(self, request, user):
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.save()

class MyCustomSignupForm(SignupForm):
    '''Добавление своих полей в форму регистрации'''
    first_name = forms.CharField(max_length=30, label='Имя',
                                 widget=forms.TextInput(attrs={'placeholder':('Имя'),'autofocus': 'autofocus'}))
    last_name = forms.CharField(max_length=30, label='Фамилия',
                                widget=forms.TextInput(attrs={'placeholder':('Фамилия'),'autofocus': 'autofocus'}))
    patronymic_name = forms.CharField(max_length=30, label='Отчество',
                                widget=forms.TextInput(attrs={'placeholder': ('Отчество'), 'autofocus': 'autofocus'}))

    def signup(self, request, user):
        '''Сохранение в базу данных'''
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.patronymic_name = self.cleaned_data['patronymic_name']
        user.save()
        return user
