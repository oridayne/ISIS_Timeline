from rest_framework import serializers
from entry.models import User, Tweet

class UserSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = User
        fields = ('id', 'name', 'username', 'description')


class TweetSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Tweet
        fields = ('id', 'date', 'tweet_detail', 'location', 'followers', 'status_number', 'user')