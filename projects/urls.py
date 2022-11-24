from django.urls import path
from projects import views

urlpatterns = [
    path('projects/', views.ProjectsList.as_view()),
    path('projects/<int:pk>/', views.ProjectsDetail.as_view()),
]
