from rest_framework import serializers
from .models import SocialUser, FriendRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialUser
        fields = ['id', 'email', 'first_name', 'last_name']

class FriendRequestSerializer(serializers.ModelSerializer):
    from_user = UserSerializer(read_only=True)
    to_user = UserSerializer(read_only=True)

    class Meta:
        model = FriendRequest
        fields = ['id', 'from_user', 'to_user', 'status', 'timestamp']