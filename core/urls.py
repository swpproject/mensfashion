from django.urls import path,include
from .views import homepage,aboutpage,contactpage
urlpatterns = [
    path('',homepage, name="home"),
    path('about/',aboutpage , name='about'),
    path('contact/',contactpage , name='contact'),
]