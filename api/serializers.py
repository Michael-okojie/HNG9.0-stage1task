from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            'slackUsername',
            'backend',
            'age',
            'bio'
        ]
