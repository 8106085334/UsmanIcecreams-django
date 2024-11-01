from django.contrib import admin
from django.urls import path 
from home import views

admin.site.site_header = "Usman Icecreams Admin Header"

# Change the admin site title (the text displayed in the browser's title bar)
admin.site.site_title = "Usman Icecreams Admin Title"

# Change the index title (the text displayed on the admin homepage)
admin.site.index_title = "Welcome to Usman Icecreams"

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name = 'about'),
    path("services",views.services, name= 'services'),
    path("contact",views.contact,name='contact')
]
