from django.db import models
from myuser.models import MyUser

# Create your models here.
class UserTracer(models.Model):
    user_id = models.ForeignKey(MyUser,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length= 200, null=True)
    ip_adress = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    desc = models.TextField(null=True)