from multiprocessing import get_context
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import sys
from frontend.forms import *
from frontend.models import *
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.conf import settings
from django.contrib import messages
from django.db.models import Count, Q

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import(
    ListView, DetailView,
    CreateView, FormView,
    TemplateView, View
)




class Home(TemplateView):
    template_name = 'frontend/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['four'] = FourApp.objects.all()
       
        return context
       

def about(request):
    team=Team.objects.all()
    about =About.objects.all()
    return render(request, 'frontend/about.html', {'tem': team, 'abt' : about})

def service(request):
    form = DriverForm()
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form = form.save()
            messages.success(request, 'Your form have been submited, Thanks for choosing Transtura')
    return render(request, 'frontend/service.html', {'form': form})

def support(request):
    support = Support2.objects.all()

    form = SupportForm()
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            form = form.save()
            messages.success(request, 'Ynks for choosing Transtura')
    return render(request, 'frontend/support.html', {'form': form, 'support' : support})



def hire(request):
    form = HireForm()
    if request.method == 'POST':
        hire_form = HireForm(request.POST)
        if hire_form.is_valid():
            hire_form = form.save()
            messages.success(request, 'User edited successfully.')
    return render(request, 'frontend/hire.html',{'hire_form':hire_form})

def contact(request):
    return render(request, 'frontend/contact.html')