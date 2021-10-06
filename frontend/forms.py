from django import forms
from frontend.models import *
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
   

   
class DriverForm(forms.ModelForm):

    class Meta():
        model = Driver
        fields = "__all__"
   
        
        widgets = {
            'pst_firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter FirstName'}), 
            'pst_lastname':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter LasttName'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter PhoneNumber'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '@gmail.com'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'home': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Home Address'}),
            'driver': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Driver License No'}),
            'nin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter NIN Number'}),
           
            
        }

class SupportForm(forms.ModelForm):

    class Meta():
        model = Support
        fields = "__all__"
       
       
        
        widgets = {
            'pst_firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter FirstName'}), 
            'pst_lastname':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter LasttName'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter PhoneNumber'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input','data-target': '#datetimepicker1'}),
            'pickoff': forms.TextInput(attrs={'class': 'form-control'}),
            'dropoff': forms.TextInput(attrs={'class': 'form-control'}),
            'drop_time': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input','data-target': '#datetimepicker1'}),
            'bus_no': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

   
class HireForm(forms.ModelForm):

    class Meta():
        model = Hire
        
        fields = "__all__"
        
        widgets = {
            'pst_firstname':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter FirstName'}), 
            'pst_lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter LasttName'}),
            'from_where' :forms.TextInput(attrs={'class': 'form-control'}),
            'to_where' :forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter PhoneNumber'}),
            'email':forms.TextInput(attrs={'class': 'form-control', 'placeholder': '@gmail.com'}),
            'passng':forms.NumberInput(attrs={'class' :'form-control'})
                   
            
        }




