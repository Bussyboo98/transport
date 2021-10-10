from django.urls import path
from frontend import views

app_name = 'frontend'

urlpatterns = [
    path('about-page/', views.about, name='about'),
    path('service-page/', views.service, name='service'),
    path('support-page/', views.support, name='support'),
    path('hire-page/', views.hire, name='hire'),
    path('career-page/', views.career, name='career'),
    path('blog-page/', views.blog, name='blog'),
    path('privacy-page/', views.privacy, name='privacy'),
    path('terms-page/', views.terms, name='terms'),
    path('post-page/<int:pk>/', views.blog_details, name='blog_details'),
    path('search-page/', views.search, name='search'),
]
