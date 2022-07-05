from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.
def Audio_store(request):
    if request.method == 'POST': 
        form = forms.AudioForm(request.POST,request.FILES or None) 
        if form.is_valid(): 
            form.save() 
            return render(request,'success.html')
    else: 
        form = forms.AudioForm() 
    return render(request, 'aud.htm', {'form' : form}) 
def redir(request):
    return render(request,'success.html')