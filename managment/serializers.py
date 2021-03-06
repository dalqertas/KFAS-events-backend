from rest_framework import serializers
from django.contrib.auth.models import User

from managment.models import Event, Attendee


class EventList(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventCreate(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ['created_by']


class EventAttendees(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        exclude = ['event']


class AttendeeRegister(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        exclude = ['event', 'did_attend']


class AttendeeInfo(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = '__all__'


class CheckIn(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = ['did_attend']


class OrganizerRegister(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['password', 'username', 'email']

    def create(self, validated_data):
        password = validated_data['password']
        username = validated_data['username']
        email = validated_data['email']

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        return validated_data
