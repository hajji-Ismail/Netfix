from django.shortcuts import render
from Auth import models

def register(request) :
 return render(request , 'Auth/register.html')
