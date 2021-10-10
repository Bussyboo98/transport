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
    
    support_form = SupportForm()
    if request.method == 'POST':
        support_form = SupportForm(request.POST)
        if support_form.is_valid():
            support_form = support_form.save()
            messages.success(request, 'Ynks for choosing Transtura')
    return render(request, 'frontend/support.html', {'support_form':support_form, 'support' : support})



def hire(request):
    hire_form = HireForm()
    if request.method == 'POST':
        hire_form = HireForm(request.POST)
        if hire_form.is_valid():
            hire_form = hire_form.save()
            messages.success(request, 'You have requested for a Bus.Our Team Will Reach Out To You Within The Next 3hrs')
    return render(request, 'frontend/hire.html',{'hire_form':hire_form})

def career(request):
    car = Career.objects.all()
    return render(request, 'frontend/career.html', {'car' : car})

def blog(request):
    blog_post =  Blog.objects.order_by('-created')
    count_post = Blog.objects.filter().count()    
    most_recent = Blog.objects.order_by('created')[:4]
    paginated_filter = Paginator(blog_post, 6)
    page_number = request.GET.get('page')
    comments = Comment.objects.filter()
    person_page_obj = paginated_filter.get_page(page_number)

    context = {
        'person_page_obj': blog_post, 
        'most_recent': most_recent,
        'counts': count_post,
        'comm':comments
    }
    context['person_page_obj'] = person_page_obj  
    

    return render(request, 'frontend/blog-home.html', context)

def blog_details(request,pk):
    single_post = get_object_or_404(Blog,pk=pk)
    comments = Comment.objects.filter(post=pk).order_by('-created_on')
    most_recent = Blog.objects.order_by('created')[:4]
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.post = single_post
            comment.save()
           
            return redirect('frontend:blog_details',pk=single_post.pk)
    else:
        form = CommentForm()     

    return render(request, 'frontend/blog-details.html',{
        
        'form':form,
        'sipst':single_post, 
        'comm': comments,
        'most_recent':most_recent
    
      
        })

def search(request):
    queryset = Blog.objects.all()
    query = request.GET.get('q')
    most_recent = Blog.objects.order_by('created')[:6]
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset,
        'most_recent':most_recent
    
        
    }
    return render(request, 'frontend/search_results.html', context)


def privacy(request):
    privacy=Privacy.objects.all()
    return render(request, 'frontend/privacy.html',{'privacy':privacy})

def terms(request):
    terms=Privacy.objects.all()
    return render(request, 'frontend/terms.html',{'terms':terms})

