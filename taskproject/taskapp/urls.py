from django.contrib import admin
from django.urls import path, include

from taskapp import views

urlpatterns = [
    path('', views.demo, name='demo'),
    # path('', views.demo_old, name='demo'),
    # path('',views.home,name='home'),
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact'),
    # path('details/',views.details,name='details'),
    # path('thanks/',views.thanks,name='thanks'),
    #
    # path('calculation/',views.caluculate),

]