from rest_framework import serializers

from .models import Conference, Location, ParticipationCondition, PresentationResult, Profile, Registration, Review


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = '__all__'

class ParticipationConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipationCondition
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class PresentationResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresentationResult
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
