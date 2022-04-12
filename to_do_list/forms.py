from django import forms

from .models import(
    To_do,
)

class To_doForm(forms.ModelForm):
    class Meta:
        model = To_do
        fields = (
            'deadline',
            'task'
        )
