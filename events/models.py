from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Event(models.Model):

    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='organized_events'
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    location = models.CharField(max_length=255)

    date = models.DateField()

    time = models.TimeField()

    capacity = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def seats_taken(self):
        return self.registrations.count()

    @property
    def seats_left(self):
        return max(self.capacity - self.seats_taken, 0)

    @property
    def is_full(self):
        return self.seats_left == 0

    @property
    def is_past(self):
        return self.date < timezone.localdate()

    def __str__(self):
        return self.title
