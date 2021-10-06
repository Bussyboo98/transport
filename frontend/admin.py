from django.contrib import admin
from frontend.models import *
from django.utils.html import format_html


admin.site.site_header = 'Transtura'



@admin.register(FourApp)
class FourAppAdmin(admin.ModelAdmin):
    def post_img(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.app_img.url))

    post_img.short_description = 'FourApp'

    list_display = [
        'title',
        'post_img',
        

        ]
   
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    def team_img(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.abt_img.url))

    team_img.short_description = 'Team'

    list_display = [
        'name',
        'title',
        'team_img',
        'created'
        ]

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    def abt_img(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.about_img.url))

    abt_img.short_description = 'About'

    list_display = [

        'title',
        'abt_img',
        'created'
        ]
   


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = [

       'pst_firstname',
       'pst_lastname',
       'email',
       'state',
       'home',
       'created',
        ]

@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = [

       'pst_firstname',
       'pst_lastname',
       
       'created',
        ]

@admin.register(Support2)
class Support2Admin(admin.ModelAdmin):
    list_display = [

       'title'
        ]

@admin.register(Hire)
class HireAdmin(admin.ModelAdmin):
    list_display = [

       'pst_firstname',
       'pst_lastname',
       'from_where',
       'to_where',
       'phone'
        ]
