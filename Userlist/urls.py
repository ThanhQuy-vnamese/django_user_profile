from django.urls import path

from . import views

urlpatterns = [
    path('api/users', views.ListCreateUserView.as_view()),
    path('api/users/create', views.ListCreateUserView.as_view()),
    path('api/users/update/<int:pk>', views.UpdateUserView.as_view()),
    path('api/users/orders', views.ListOrderView.as_view()),
    path('api/users/orders/<int:pk>', views.ListUpdateOrderView.as_view()),
    path('api/users/profile/', views.ListCreateProfileView.as_view()),
    path('api/users/create/profile/<int:pk>', views.ListCreateProfileView.as_view()),
    path('api/users/update/profile/<int:pk>', views.UpdateProfileView.as_view()),
]