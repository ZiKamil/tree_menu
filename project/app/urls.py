from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuListView.as_view(), name='menu'),
    path('menu/<int:pk>', views.MenuDetailView.as_view(), name='menu-detail'),
]
