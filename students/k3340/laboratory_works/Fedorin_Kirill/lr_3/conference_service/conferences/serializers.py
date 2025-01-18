from datetime import date

from rest_framework import serializers

from .models import Conference, ConferenceDashboard, CustomUser, Location, ParticipationCondition, PresentationResult, Registration, Review


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'birthday', 'work_education')
        required_fields = ('username', 'password', 'email', 'first_name', 'last_name')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'



class ConferenceSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    participants = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    ) 

    class Meta:
        model = Conference
        fields = '__all__'

class ConferenceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        exclude = ('participants',) 


class RegistrationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    conference = serializers.PrimaryKeyRelatedField(queryset=Conference.objects.all())

    class Meta:
        model = Registration
        fields = '__all__'

    def validate(self, data):
        conference = data['conference']
        if conference.end_date < date.today():
            raise serializers.ValidationError("Регистрация на уже прошедшие мероприятия невозможна.")
        return data

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    conference = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = '__all__'

    def validate(self, data):
        conference = data['conference']
        if conference.end_date >= date.today():
            raise serializers.ValidationError("Отзывы можно оставлять только после окончания мероприятия.")
        return data

class PresentationResultSerializer(serializers.ModelSerializer):
    registration = RegistrationSerializer()

    class Meta:
        model = PresentationResult
        fields = '__all__'

class ConferenceDashboardSerializer(serializers.ModelSerializer):
    conference = serializers.StringRelatedField()

    class Meta:
        model = ConferenceDashboard
        fields = ('conference', 'total_registrations', 'average_rating')

class ParticipationConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipationCondition
        fields = '__all__'


