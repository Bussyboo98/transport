
from django.db import models
from django.db.models import Q
from django.db.models.fields.files import ImageField
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from tinymce import HTMLField
from django.utils.html import format_html
from fontawesome_5.fields import IconField
import datetime



class FourApp(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=300)
    app_img =  models.ImageField(upload_to='uploads/', blank=True, null=True)


    def __str__(self):
        return self.title

    class Meta():
        verbose_name_plural = 'FourApp'

    def post_img(self):
        if self. app_img:
          return self.app_img.url



  


class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name="Founder Nmae")
    title= models.CharField(max_length=100, verbose_name="Designation")
    abt_img =  models.ImageField(upload_to='uploads/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, help_text='This will automatically add a time when you click save')
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Team'

    def team_img(self):
        if self.abt_img:
          return self.abt_img.url

class About(models.Model):
    title= models.CharField(max_length=100)
    about_img =  models.ImageField(upload_to='uploads/', blank=True, null=True)
    content = HTMLField('Content')
    mission= models.CharField(max_length=100, verbose_name="Mission Title")
    content1 = models.TextField(max_length=300)
    vision= models.CharField(max_length=100, verbose_name="Vision Title")
    content2 = models.TextField(max_length=300)
   
    created = models.DateTimeField(auto_now_add=True, help_text='This will automatically add a time when you click save')
    modified = models.DateTimeField(auto_now=True)
  

    def __str__(self):
        return self.title

    class Meta():
        verbose_name_plural = 'About Us'

    def abt_img(self):
        if self.about_img:
          return self.about_img.url



class Driver(models.Model):
   
    pst_firstname = models.CharField(max_length=150, verbose_name= 'First Name')
    pst_lastname = models.CharField(max_length=150, verbose_name= 'Last Name')
    email = models.CharField(max_length=40,)
    phone = models.CharField(max_length=50, verbose_name='Phone')
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    home = models.CharField(max_length=200, verbose_name="Home Address")
    driver = models.CharField(max_length=100, verbose_name="Drivers License No")
    nin = models.CharField(max_length=100, verbose_name="NIN No")
    created = models.DateTimeField(auto_now_add=True, help_text='This will automatically add a time when you click save')
    modified = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return self.pst_firstname

    class Meta():
        verbose_name_plural = 'Driver'


class Support(models.Model):
   
    pst_firstname = models.CharField(max_length=150, verbose_name= 'First Name')
    pst_lastname = models.CharField(max_length=150, verbose_name= 'Last Name')
    phone = models.CharField(max_length=50, verbose_name='Phone')
    date = models.CharField(max_length=200, verbose_name="Date/Time")
    pickoff = models.CharField(max_length=200, verbose_name="Pickoff Location")
    dropoff = models.CharField(max_length=100, verbose_name="Dropoff Location")
    drop_time= models.CharField(max_length=200, verbose_name="Date/Time")
    bus_no = models.CharField(max_length=100, verbose_name="Bus Serial No")
    created = models.DateTimeField(auto_now_add=True, help_text='This will automatically add a time when you click save')
    modified = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return self.pst_firstname

    class Meta():
        verbose_name_plural = 'Support'


class Support2(models.Model):
    title = models.CharField(max_length=10)
    content = HTMLField('Content')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name_plural = 'Support Content'


class Hire(models.Model):
   
    pst_firstname = models.CharField(max_length=150, verbose_name= 'First Name')
    pst_lastname = models.CharField(max_length=150, verbose_name= 'Last Name')
    email = models.CharField(max_length=40,)
    phone = models.CharField(max_length=50, verbose_name='Phone')
    from_where = models.CharField(max_length=200, verbose_name='From Where')
    to_where = models.CharField(max_length=200, verbose_name='Where arae you going')
    passng = models.IntegerField(verbose_name="No of Passenger")
    da_ti = models.CharField(max_length=200, verbose_name="Date/Time")
   
   

    def __str__(self):
        return self.pst_firstname

    class Meta():
        verbose_name_plural = 'Hire'


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Post Title')
    slug = models.SlugField(unique=True)
    blg_image = models.ImageField(null=True, verbose_name='Blog Image', blank=True, upload_to='uploads/')
    content = HTMLField('Content')
    blg_image1 = models.ImageField(null=True, verbose_name='Blog Image1', blank=True, upload_to='uploads/')
    blg_image2 = models.ImageField(null=True, verbose_name='Blog Image2', blank=True, upload_to='uploads/')
    
    user = models.CharField(max_length=100, verbose_name="Posted By")
    created = models.DateTimeField(auto_now_add=True, help_text='This will automatically add a time when you click save')
    modified = models.DateTimeField(auto_now=True)
    time = models.DateTimeField(auto_now_add=True)
    today = datetime.date.today()
    months = ['zero','January','February','March','April','May','June','July','August','September','October','November','December']
    current_month = months[today.month]

    def __str__(self):
        return self.title

    class Meta():
        verbose_name_plural = 'Blog'

    def blog_img(self):
        if self.blg_image:
          return self.blg_image.url

    def blog_img1(self):
        if self.blg_image1:
          return self.blg_image1.url
    
    def blog_img2(self):
        if self.blg_image2:
          return self.blg_image2.url

    @property
    def get_comments(self):
        return self.comments.all()

    def get_post_url(self):
        return reverse('frontend:blog_details', kwargs={
            'slug': self.slug,
        })


class Comment(models.Model):
    name = models.CharField(max_length=80,verbose_name= 'Name')
    email = models.EmailField()
    website = models.CharField(max_length=100)
    body = HTMLField('Content')
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)

    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    class Meta():
        verbose_name_plural = 'Comments'


    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class Career(models.Model):
    car_image = models.ImageField(null=True, verbose_name='Career Image', blank=True, upload_to='uploads/')
    content = HTMLField('Content')
    created = models.DateTimeField(auto_now_add=True, help_text='This will automatically add a time when you click save')
    modified = models.DateTimeField(auto_now=True)
   

   
    class Meta():
        verbose_name_plural = 'Career'

    def car_img(self):
        if self.car_image:
            return self.car_image.url

class Privacy(models.Model):
    title= models.CharField(max_length=100)
    content = HTMLField('Privacy Policy')
    content2 = HTMLField('Terms & Conditions')
    created = models.DateTimeField(auto_now_add=True, help_text='This will automatically add a time when you click save')
    modified = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.title
   
    class Meta():
        verbose_name_plural = 'Privacy'

    

