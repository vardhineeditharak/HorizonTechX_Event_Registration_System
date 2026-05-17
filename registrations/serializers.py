from rest_framework import serializers
from .models import Registration

class RegistrationSerializer(serializers.ModelSerializer):
    event_title = serializers.ReadOnlyField(source='event.title')
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Registration
        fields = ['id', 'user', 'username', 'event', 'event_title', 'registered_at']
        read_only_fields = ['user']

    def validate_event(self, event):
        request = self.context.get('request')

        if event.is_past:
            raise serializers.ValidationError('You cannot register for a past event.')

        if event.is_full:
            raise serializers.ValidationError('This event is already full.')

        if request and request.user.is_authenticated:
            exists = Registration.objects.filter(
                user=request.user,
                event=event
            ).exists()
            if exists:
                raise serializers.ValidationError('You are already registered for this event.')

        return event
