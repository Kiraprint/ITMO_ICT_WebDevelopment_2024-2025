from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
   ConferenceCreateViewSet,
   ConferenceDashboardViewSet,
   ConferenceViewSet,
   CustomUserCreateViewSet,
   CustomUserViewSet,
   LocationViewSet,
   ParticipationConditionViewSet,
   PresentationResultViewSet,
   RegistrationViewSet,
   ReviewViewSet,
)

router = DefaultRouter()
router.register(r'register', CustomUserCreateViewSet, basename='register')
router.register(r'locations', LocationViewSet)
router.register(r'conferences', ConferenceViewSet)
router.register(r'conferences_create', ConferenceCreateViewSet, basename='conferences_create')
router.register(r'conditions', ParticipationConditionViewSet)
router.register(r'registrations', RegistrationViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'results', PresentationResultViewSet)
router.register(r'profiles', CustomUserViewSet, basename='user')
router.register(r'conference-dashboard', ConferenceDashboardViewSet)


urlpatterns = [
   path('', include(router.urls)),
]
