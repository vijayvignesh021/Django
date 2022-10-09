from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from firstapp import urls,views
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',include('firstapp.urls')),
    path('',include('firstapp.urls')),
]

