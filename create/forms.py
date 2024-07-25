from django import forms
from .models import Employee


class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['ful_name', 'emo_code', 'mobile', 'postion']


    def __init__(self, *args, **kwargs):
        super(EmployeForm, self).__init__(*args, **kwargs)
        self.fields['postion'].empty_label = "Select"