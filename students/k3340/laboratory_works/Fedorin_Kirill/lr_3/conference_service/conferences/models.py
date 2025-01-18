from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    work_education = models.CharField(max_length=100, blank=True)

class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=512)
    description = models.TextField()

    def __str__(self):
        return self.name

class Conference(models.Model):
    title = models.CharField(max_length=255)
    topics = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    participants = models.ManyToManyField('CustomUser', through='Registration')


    def __str__(self):
        return self.title

class ParticipationCondition(models.Model):
    conference = models.OneToOneField(Conference, on_delete=models.CASCADE)
    conditions = models.TextField()

    def __str__(self):
        return f'Conditions for {self.conference.title}'

class Registration(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    registered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} registered for {self.conference.title}'

class Review(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)])
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.conference.title}'

class PresentationResult(models.Model):
    registration = models.OneToOneField(Registration, on_delete=models.CASCADE)
    is_recommended_for_publication = models.BooleanField(default=False)

    def __str__(self):
        return f'Result for {self.registration}'

class ConferenceDashboard(models.Model):
    conference = models.OneToOneField(Conference, on_delete=models.CASCADE)
    total_registrations = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0.0)

    def update_dashboard(self):
        registrations = Registration.objects.filter(conference=self.conference).count()
        self.total_registrations = registrations
        reviews = Review.objects.filter(conference=self.conference)
        self.average_rating = reviews.aggregate(models.Avg('rating'))['rating__avg'] or 0.0
        self.save()

    def __str__(self):
        return f'Dashboard for {self.conference.title}'