from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from events.views import (
    EventCreatePage,
    EventDeletePage,
    EventUpdatePage,
    event_detail_page,
    event_list_page,
)
from registrations.views import (
    cancel_registration_page,
    my_registrations_page,
    register_for_event_page,
)
from users.views import logout_page, signup_page

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('', event_list_page, name='event-list-page'),
    path('events/new/', EventCreatePage.as_view(), name='event-create-page'),
    path('events/<int:pk>/edit/', EventUpdatePage.as_view(), name='event-edit-page'),
    path('events/<int:pk>/delete/', EventDeletePage.as_view(), name='event-delete-page'),
    path('events/<int:pk>/', event_detail_page, name='event-detail-page'),
    path(
        'events/<int:event_id>/register/',
        register_for_event_page,
        name='event-register-page'
    ),
    path(
        'registrations/<int:pk>/cancel/',
        cancel_registration_page,
        name='registration-cancel-page'
    ),
    path(
        'my-registrations/',
        my_registrations_page,
        name='my-registrations-page'
    ),
    path('signup/', signup_page, name='signup-page'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path('logout/', logout_page, name='logout-page'),

    path('admin/', admin.site.urls),

    path('api/events/',
         include('events.urls')),

    path('api/registrations/',
         include('registrations.urls')),

    path('api/users/',
         include('users.urls')),

    path('api/token/',
         TokenObtainPairView.as_view()),

    path('api/token/refresh/',
         TokenRefreshView.as_view()),
]
