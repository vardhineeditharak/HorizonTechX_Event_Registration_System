from django.urls import path
from .views import *

urlpatterns = [
    path('', RegisterEventView.as_view()),
    path('<int:pk>/', RegistrationDetailView.as_view()),
]
