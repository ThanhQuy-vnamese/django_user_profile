from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import User, Order, Profile
from .serializers import UserSerializer, OrderSerializer, ProfileSerializer


# from django.contrib.auth.models import User


class ListCreateUserView(ListCreateAPIView):
    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new User successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new User unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserView(RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def put(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs.get('pk'))
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update User successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update User unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs.get('pk'))
        user.delete()

        return JsonResponse({
            'message': 'Delete User successful!'
        }, status=status.HTTP_200_OK)


class ListOrderView(ListCreateAPIView):
    model = Order
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Order successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Order unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)


class ListUpdateOrderView(RetrieveUpdateDestroyAPIView):
    model = Order
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()

    def put(self, request, *args, **kwargs):
        order = get_object_or_404(Order, id=kwargs.get('pk'))
        serializer = OrderSerializer(order, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Order successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Order unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        order = get_object_or_404(Order, id=kwargs.get('pk'))
        order.delete()

        return JsonResponse({
            'message': 'Delete Order successful!'
        }, status=status.HTTP_200_OK)


class ListCreateProfileView(ListCreateAPIView):
    model = Profile
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.all()

    def create(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs.get('pk'))
        Profile.user = user
        serializer = ProfileSerializer(Profile.user, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)


class UpdateProfileView(RetrieveUpdateDestroyAPIView):
    model = Profile
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.all()

    def put(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, user_id=kwargs.get('pk'))
        serializer = ProfileSerializer(profile, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, user_id=kwargs.get('pk'))
        profile.delete()

        return JsonResponse({
            'message': 'Delete successful!'
        }, status=status.HTTP_200_OK)
