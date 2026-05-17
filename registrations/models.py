from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from events.models import Event

class Registration(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='registrations'
    )

    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')

    def clean(self):
        if self.event_id and self.event.is_past:
            raise ValidationError('You cannot register for a past event.')

        if self.event_id and not self.pk and self.event.is_full:
            raise ValidationError('This event is already full.')

    def __str__(self):
        return f"{self.user.username} -> {self.event.title}"
