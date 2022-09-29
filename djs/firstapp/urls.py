from django.urls import path,include
from . import views

urlpatterns = [
    path('num/',views.num,name='num'),
    path('',views.inx),
    path('login/',views.login,name='login'),
]