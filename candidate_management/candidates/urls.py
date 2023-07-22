from django.urls import path
from . import views

urlpatterns = [
    path('', views.candidate_list, name='candidate_list'),
    path('add/', views.add_candidate, name='add_candidate'),
    path('<int:pk>/', views.candidate_detail, name='candidate_detail'),
    path('<int:pk>/edit/', views.edit_candidate, name='edit_candidate'),
    path('<int:pk>/delete/', views.delete_candidate, name='delete_candidate'),
]
