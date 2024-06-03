
from django.urls import path
from .views import *
app_name='app1'

urlpatterns = [
    path('register/',register,name='register'),
    path('home/',home,name='home'),
    path('logout/',logout_view,name='logout'),
    path('login/',login_view,name='login'),

]
