from rest_framework import serializers
from django.utils import timezone

from .models import Event

class EventSerializer(serializers.ModelSerializer):

    organizer = serializers.ReadOnlyField(
        source='organizer.username'
    )

    class Meta:
        model = Event
        fields = '__all__'

    def validate_date(self, date):
        if date < timezone.localdate():
            raise serializers.ValidationError('Event date cannot be in the past.')
        return date

    def validate_capacity(self, capacity):
        if capacity < 1:
            raise serializers.ValidationError('Capacity must be at least 1.')
        return capacity
