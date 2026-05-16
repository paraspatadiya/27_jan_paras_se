from django import forms
from .models import doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = doctor
        fields = '__all__'
        