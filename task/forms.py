from django import forms
from django.forms import ModelForm, extras
from django.contrib.auth.models import User
from .models import Label
from django.contrib.admin.widgets import AdminDateWidget


class SignUpForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']


class SignInForm(forms.Form):
    username = forms.CharField(label='username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class AddTaskForm(forms.Form):
    TYPE_OF_PRIORITY = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    task_name = forms.CharField(label='task name', max_length=1000)
    task_description = forms.CharField(label='task description', max_length=10000)
    expiry_date = forms.DateField(widget=extras.SelectDateWidget)
    label = forms.ModelChoiceField(queryset=Label.objects.all())
    priority = forms.CharField(label='Priority', widget=forms.Select(choices=TYPE_OF_PRIORITY))

