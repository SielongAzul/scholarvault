from django.shortcuts import render
from .models import Scholarships


def home(request):

    scholarships = Scholarships.objects.all()
    context = {'scholarship':scholarships}
    return (render) (request, 'scholarship/home.html', context)

#context = {'name of context for views', what you declared in models.py}


def account_login(request):
    return (render) (request, 'scholarship/login_form.html')