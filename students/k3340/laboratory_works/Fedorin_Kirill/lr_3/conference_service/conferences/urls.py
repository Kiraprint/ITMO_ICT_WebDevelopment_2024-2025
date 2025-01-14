from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ConferenceViewSet, LocationViewSet, ParticipationConditionViewSet, PresentationResultViewSet, ProfileViewSet, RegistrationViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'conferences', ConferenceViewSet)
router.register(r'conditions', ParticipationConditionViewSet)
router.register(r'registrations', RegistrationViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'results', PresentationResultViewSet)
router.register(r'profiles', ProfileViewSet)


urlpatterns = [
   path('', include(router.urls)),
]
