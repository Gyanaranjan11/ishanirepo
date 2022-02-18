from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name=models.CharField(max_length=50)
    f_name=models.CharField(max_length=50, null=True, blank=True)
    l_name=models.CharField(max_length=50, null=True, blank=True)
    dob=models.CharField(max_length=50, null=True, blank=True)
    email=models.CharField(unique=True, max_length=50, blank=True, null=True)
    email_verify = models.CharField(max_length=12, default="not_verified", blank=True, null=True)
    mob_no=models.CharField(unique=True, max_length=10, blank=True, null=True)
    mob_no_verify = models.CharField(max_length=12, default="not_verified", blank=True, null=True)
    password=models.CharField(max_length=30, blank=True, null=True)
    gender=models.CharField(max_length=10, blank=True, null=True)
    status=models.CharField(max_length=10, default="active", blank=True, null=True)
    p_status=models.CharField(max_length=10, blank=True, null=True)
    photo=models.ImageField(upload_to='user/photo', blank=True, null=True)
    created_date=models.DateField(blank=True, null=True)
    modify_date=models.DateField(auto_now_add=True,blank=True, null=True)
    deleted_date=models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


