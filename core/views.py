import core
from django.shortcuts import render,HttpResponseRedirect
from .forms import Resumeforms
from .models import Resumemodel
from django.contrib import messages
# Create your views here.
def Home(request):
    context={'name':'active'}
    return render(request,'home.html',context)

def contact(request):
    if request.method == 'POST':
        fm = Resumeforms(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            sb = fm.cleaned_data['subject']
            ms = fm.cleaned_data['message']
            clean = Resumemodel(name=nm,email= em,subject=sb,message = ms)
            clean.save()
            messages.success(request, 'SUCCESS: form submitted successfully...')
            return HttpResponseRedirect('/')
    else:
        fm = Resumeforms()        
    return render(request,'contact.html',{'contact':'active','form':fm})
