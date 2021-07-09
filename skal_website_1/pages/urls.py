from django.urls import path
from .views import show_home_page, show_about_page


urlpatterns = [
    path('',show_home_page,name='home_page'),
    path('about/',show_about_page,name='about_page'),
]

