from rest_framework import serializers
from .models import SocialUser, FriendRequest
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialUser
        fields = ['id', 'email', 'user', 'first_name', 'last_name']
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def create(self, validated_data):
        email = validated_data['email']
        first_name = validated_data.get('first_name', '')
        last_name = validated_data.get('last_name', '')

        user = User.objects.create(username=email, email=email, first_name=first_name, last_name=last_name)
        user.set_password('default')
        user.save()

        social_user = SocialUser.objects.create(user=user, **validated_data)
        return social_user

class FriendRequestSerializer(serializers.ModelSerializer):
    from_user = UserSerializer(read_only=True)
    to_user = UserSerializer(read_only=True)

    class Meta:
        model = FriendRequest
        fields = ['id', 'from_user', 'to_user', 'status', 'timestamp']