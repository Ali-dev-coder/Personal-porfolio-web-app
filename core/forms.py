from django import forms
from .models import Resumemodel
class Resumeforms(forms.ModelForm):
    class Meta:
        model=Resumemodel
        fields = '__all__'
        labels = {'name':'Your Name','email':'Your Email'}
        error_messages = {'name':{'required':'please enter name'}, 'email':{'required':'please enter email'},'subject':{'required':'Must Enter Subject of form'},'message':{'required':'please enter message'},}
        widgets = {'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Your Name'}),
        'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Your Email'}),
        'subject':forms.TextInput(attrs={'class':'form-control','placeholder':'Write Subject Here'}),
        'message':forms.Textarea(attrs={'class':'form-control','placeholder':'Write Message Here..........'}),}
