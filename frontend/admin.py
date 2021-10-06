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
       'phone',
       'pickoff',
       'dropoff',
       'bus_no'
       
      
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


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    def blog_img(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.blg_image.url))

    blog_img.short_description = 'Blog'

    list_display = [

        'blg_title',
        'blog_img',
        'created'
        ]
   
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body',  'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    def car_img(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.car_image.url))

    car_img.short_description = 'Career'

    list_display = [
        'car_img',
        'created'
        ]

@admin.register(Privacy)
class PrivacyAdmin(admin.ModelAdmin):
    list_display = [

       'title',
       
       
      
        ]

   
