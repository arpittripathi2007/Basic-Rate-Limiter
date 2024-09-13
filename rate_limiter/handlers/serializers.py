from .models import User, RateLimitUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'rate_limit']


class RegisterSerializer(serializers.ModelSerializer):
    rate_limit = serializers.IntegerField(default=100)

    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'rate_limit')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            rate_limit=validated_data['rate_limit']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user