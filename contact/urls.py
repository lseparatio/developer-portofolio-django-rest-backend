from django.urls import path
from contact import views

urlpatterns = [
    path('contact/', views.ContactForm.as_view()),
    path('contact-messages/', views.ContactMessages.as_view()),
    path('contact-messages/<int:pk>/', views.ContactDetail.as_view()),
]
