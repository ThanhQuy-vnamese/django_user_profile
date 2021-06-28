from rest_framework import serializers
from .models import Profile
from .models import User
from .models import Order


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user_id', 'company', 'company_phone')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'phone')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'price', 'order_description', 'create_at', 'update_at', 'user')
