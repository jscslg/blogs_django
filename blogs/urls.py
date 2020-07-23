from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name="home-page"),
    path('',views.about_view,name="about-page"),
]