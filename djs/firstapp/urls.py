<<<<<<< HEAD
from django.urls import path,include
from . import views

urlpatterns = [
    path('num/',views.num,name='num'),
    path('',views.inx),
    path('login/',views.login,name='login'),
=======
from django.urls import path,include
from . import views

urlpatterns = [
    path('num/',views.num,name='num'),
    path('',views.inx),
    path('login/',views.login,name='login'),
>>>>>>> 58c2781f6e12362f31ad786b6796c2773cf0ab3e
]