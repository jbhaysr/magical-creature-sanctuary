from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreatureListView.as_view(), name='creature_list'),
    path('<int:pk>/', views.CreatureDetailView.as_view(), name='creature_detail'),
]