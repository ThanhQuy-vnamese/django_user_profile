from django.db import models

# Create your models here


class User(models.Model):

    objects = None
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True)
    company = models.CharField(max_length=100, null=True)
    company_phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return 'Profile of user id:{0} created'.format(self.user_id)


class Order(models.Model):

    objects = None
    id = models.AutoField(primary_key=True)
    price = models.FloatField(default=0)
    order_description = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_created=True, null=False)
    update_at = models.DateTimeField(auto_now_add=True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Order id: ' + str(self.id) + '' + 'by User: ' + str(self.user) + 'created at: ' + str(self.create_at)
