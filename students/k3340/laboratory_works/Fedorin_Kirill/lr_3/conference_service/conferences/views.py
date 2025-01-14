from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny

from .models import Conference, Location, ParticipationCondition, PresentationResult, Profile, Registration, Review
from .serializers import (
    ConferenceSerializer,
    LocationSerializer,
    ParticipationConditionSerializer,
    PresentationResultSerializer,
    ProfileSerializer,
    RegistrationSerializer,
    ReviewSerializer,
)


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ConferenceViewSet(viewsets.ModelViewSet):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer
    permission_classes = [AllowAny]
    ordering_fields = ['start_date', 'end_date']
    ordering = ['start_date']  # Default ordering
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'location', 'start_date']

class ParticipationConditionViewSet(viewsets.ModelViewSet):
    queryset = ParticipationCondition.objects.all()
    serializer_class = ParticipationConditionSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class PresentationResultViewSet(viewsets.ModelViewSet):
    queryset = PresentationResult.objects.all()
    serializer_class = PresentationResultSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
