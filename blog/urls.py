from django.urls import path
from . import views

# assigning a view called post_list to the root URL
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]