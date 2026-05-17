from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import generics, permissions

from events.models import Event
from .models import Registration
from .serializers import RegistrationSerializer

class RegisterEventView(
    generics.ListCreateAPIView
):

    serializer_class = RegistrationSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return Registration.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class RegistrationDetailView(
    generics.RetrieveDestroyAPIView
):

    serializer_class = RegistrationSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return Registration.objects.filter(
            user=self.request.user
        )


@login_required
def my_registrations_page(request):
    registrations = Registration.objects.filter(
        user=request.user
    ).select_related('event', 'event__organizer').order_by('event__date', 'event__time')

    return render(
        request,
        'registrations/my_registrations.html',
        {'registrations': registrations}
    )


@login_required
def register_for_event_page(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method != 'POST':
        return redirect('event-detail-page', pk=event.pk)

    already_registered = Registration.objects.filter(
        user=request.user,
        event=event
    ).exists()

    if already_registered:
        messages.info(request, 'You are already registered for this event.')
    elif event.is_past:
        messages.error(request, 'Registration is closed because this event has passed.')
    elif event.registrations.count() >= event.capacity:
        messages.error(request, 'This event is already full.')
    else:
        Registration.objects.create(user=request.user, event=event)
        messages.success(request, 'Registration confirmed.')

    return redirect('event-detail-page', pk=event.pk)


@login_required
def cancel_registration_page(request, pk):
    registration = get_object_or_404(
        Registration,
        pk=pk,
        user=request.user
    )
    event_pk = registration.event.pk

    if request.method == 'POST':
        registration.delete()
        messages.success(request, 'Registration cancelled.')
        return redirect('my-registrations-page')

    return redirect('event-detail-page', pk=event_pk)
