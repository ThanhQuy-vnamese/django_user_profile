from django.urls import path

from . import views

urlpatterns = [
    path('users', views.ListCreateUserView.as_view()),
    path('users/create', views.ListCreateUserView.as_view()),
    path('users/update/<int:pk>', views.UpdateUserView.as_view()),
    path('orders', views.ListOrderView.as_view()),
    path('update_orders/<int:pk>', views.ListUpdateOrderView.as_view()),
    path('profile/', views.ListCreateProfileView.as_view()),
    path('create/profile/<int:pk>', views.ListCreateProfileView.as_view()),
    path('update/profile/<int:pk>', views.UpdateProfileView.as_view()),
]