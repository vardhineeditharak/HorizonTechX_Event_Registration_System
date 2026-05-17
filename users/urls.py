from django.urls import path

from .views import UserRegistrationView, signup_page


urlpatterns = [
    path('signup/', UserRegistrationView.as_view()),
    path('web-signup/', signup_page),
]
