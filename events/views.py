from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count, F, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from rest_framework import generics, permissions

from registrations.models import Registration
from .forms import EventForm
from .models import Event
from .permissions import IsOrganizerOrReadOnly
from .serializers import EventSerializer

class EventListCreateView(
    generics.ListCreateAPIView
):

    queryset = Event.objects.all()

    serializer_class = EventSerializer

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(
            organizer=self.request.user
        )


class EventDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = Event.objects.all()

    serializer_class = EventSerializer

    permission_classes = [
        IsOrganizerOrReadOnly
    ]


def event_list_page(request):
    query = request.GET.get('q', '').strip()
    availability = request.GET.get('availability', '').strip()

    events = Event.objects.select_related('organizer').annotate(
        registration_count=Count('registrations')
    ).order_by('date', 'time')

    if query:
        events = events.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(location__icontains=query)
            | Q(organizer__username__icontains=query)
        )

    if availability == 'open':
        events = events.filter(registration_count__lt=F('capacity'))

    return render(
        request,
        'events/event_list.html',
        {
            'events': events,
            'query': query,
            'availability': availability,
        }
    )


def event_detail_page(request, pk):
    event = get_object_or_404(
        Event.objects.select_related('organizer'),
        pk=pk
    )
    user_registration = None
    seats_taken = event.registrations.count()
    seats_left = max(event.capacity - seats_taken, 0)

    if request.user.is_authenticated:
        user_registration = Registration.objects.filter(
            user=request.user,
            event=event
        ).first()

    return render(
        request,
        'events/event_detail.html',
        {
            'event': event,
            'user_registration': user_registration,
            'seats_taken': seats_taken,
            'seats_left': seats_left,
        }
    )


class EventCreatePage(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event-list-page')

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        messages.success(self.request, 'Event created successfully.')
        return super().form_valid(form)


class OrganizerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        event = self.get_object()
        return event.organizer == self.request.user


class EventUpdatePage(OrganizerRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'

    def get_success_url(self):
        return reverse_lazy('event-detail-page', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, 'Event updated successfully.')
        return super().form_valid(form)


class EventDeletePage(OrganizerRequiredMixin, DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('event-list-page')

    def form_valid(self, form):
        messages.success(self.request, 'Event deleted successfully.')
        return super().form_valid(form)
