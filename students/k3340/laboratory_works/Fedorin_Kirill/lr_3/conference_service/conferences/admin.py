from django.contrib import admin

from .models import Conference, Location, ParticipationCondition, PresentationResult, Profile, Registration, Review

admin.site.register(Location)
admin.site.register(Conference)
admin.site.register(ParticipationCondition)
admin.site.register(Registration)
admin.site.register(Review)
admin.site.register(PresentationResult)
admin.site.register(Profile)
