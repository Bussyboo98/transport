from django.urls import path
from frontend import views

app_name = 'frontend'

urlpatterns = [
    path('about-page/', views.about, name='about'),
    path('service-page/', views.service, name='service'),
     path('support-page/', views.support, name='support'),
    path('hire-page/', views.hire, name='hire'),
    path('contact-page/', views.contact, name='contact'),
]
