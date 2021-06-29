from rest_framework import serializers
from .models import Profile
from .models import User
from .models import Order


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user_id', 'company', 'company_phone')

    def create(self, validated_data):
        profile = Profile(
            user=validated_data['user_id'],
            company=validated_data['company'],
            company_phone=validated_data['company_phone']
        )
        profile.save()
        return profile


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'phone', 'profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'price', 'order_description', 'create_at', 'update_at', 'user')
