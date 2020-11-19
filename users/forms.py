from django import forms
from .models import List


# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
#
#
class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['item', 'completed']
