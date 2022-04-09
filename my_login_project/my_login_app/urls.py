from django.urls import path
from . import views

app_name='my_login_app'

urlpatterns=[
    
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('profile/',views.profile_view,name='profile')
    ]