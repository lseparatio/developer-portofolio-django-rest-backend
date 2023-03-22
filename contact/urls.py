from django.urls import path
from contact import views

urlpatterns = [
    path('contact/', views.ContactList.as_view()),
]
