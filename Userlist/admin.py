from django.contrib import admin
from .models import Profile
from .models import User
from .models import Order
# Register your models here.

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Order)
