from datetime import date

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from .models import Conference, ConferenceDashboard, CustomUser, Location, ParticipationCondition, PresentationResult, Registration, Review
from .serializers import (
    ConferenceDashboardSerializer,
    ConferenceSerializer,
    CustomUserCreateSerializer,
    CustomUserSerializer,
    LocationSerializer,
    ParticipationConditionSerializer,
    PresentationResultSerializer,
    RegistrationSerializer,
    ReviewSerializer,
)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserCreateViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreateSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class ConferenceCreateViewSet(viewsets.ModelViewSet):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer
    permission_classes = [IsAdminUser]

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

    def perform_create(self, serializer):
        conference = serializer.validated_data['conference']
        if conference.end_date < date.today():
            return Response({"detail": "Регистрация на уже прошедшие мероприятия невозможна"}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        conference = serializer.validated_data['conference']
        if conference.end_date >= date.today():
            return Response({"detail": "Отзывы можно оставлять только после окончания мероприятия"}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()


class PresentationResultViewSet(viewsets.ModelViewSet):
    queryset = PresentationResult.objects.all()
    serializer_class = PresentationResultSerializer


class ConferenceDashboardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ConferenceDashboard.objects.all()
    serializer_class = ConferenceDashboardSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.update_dashboard()  # Automatically update dashboard metrics before fetching
        return super().retrieve(request, *args, **kwargs)
