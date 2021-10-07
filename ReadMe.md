Transtura 

To access the admin, create your superuser with the command 'python manage,py createsuperuser' but first you must 
activate your virtual enviroment. You can use the one you use or create new one, to craete new env type the command 
'conda craete --name (name of you env) python==3.7 (you can use 3.8). then install django and the dependencies in the requirement.txt

pip install django-filebrowser
pip install django-tinymce4-lite
pip install Pillow==8.3.2

once installed den craete you admin and runserver with python manage.py runserver

So have made some forms to save
ie if anyone fills the form, the forms saves in you admin so you can see the people requesting for ride or stuffs

you can also change the alert message to your choice you want .
Go to the views where you have alert message .What it does is that once some one fills the form and click submit 
the alert message pop up


def hire(request):
    hire_form = HireForm()
    if request.method == 'POST':
        hire_form = HireForm(request.POST)
        if hire_form.is_valid(): - this check if the form is valid i.e no form was left unfilled or email has @gmail.com etc
            hire_form = hire_form.save()- once its valid it saves in your database
            messages.success(request, 'You have requested for a Bus.Our Team Will Reach Out To You Within The Next 3hrs')- Tis ahows the alert message
    return render(request, 'frontend/hire.html',{'hire_form':hire_form})


something like this now  you can change the text. Though it must be in a string

So have created what you have to be doing from the admin so everything is there