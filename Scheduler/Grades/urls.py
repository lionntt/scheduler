"""learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.http import HttpResponse
from .views import learning ,form_choices ,GradesAJAX ,subject_ajax ,subject_to_test

#def Learning(request):
    # return HttpResponse("I'm homepage")


urlpatterns = [
    # url(r'^grades/$', learning),
    # url(r'^gradeform/$',form_choices),
    # url(r'^grades_ajax/$',GradesAJAX),
    path('grades/',learning),
    path('gradesform/',form_choices),
    path('grades_ajax/',GradesAJAX),
    path('grades_subject/',subject_ajax,name='grades_subject'),
    path('grades/<str:test>/', subject_to_test, name='url_test')
]
