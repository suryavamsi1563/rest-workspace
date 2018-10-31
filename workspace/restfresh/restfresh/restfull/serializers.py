from rest_framework import serializers
from .models import Polls


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length = 10)

class PollsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Polls
        fields = ('name','text','created_on')

    def create(self,validated_data):
        poll = Polls(
            name = validated_data['name'],
            text = validated_data['text'],
        )
        poll.save()
        return poll