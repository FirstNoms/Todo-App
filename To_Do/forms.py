from django import forms

from To_Do.models import UserModel, ToDoModel


class TodoForm(forms.ModelForm):
    class Meta:
        model = ToDoModel
        exclude = ['time_stamp']

class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields ='__all__'