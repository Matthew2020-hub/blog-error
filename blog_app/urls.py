from django.urls import path
from .views import BlogListView

urlspattern = [
    path('', BlogListView.as_view(), name= 'home'),

]