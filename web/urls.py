from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name='index'),
    #path('courses/', views.BookListView.as_view(), name='courses'),

    
]