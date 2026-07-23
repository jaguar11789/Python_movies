from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # auth_user 참조 1:1 매칭

    name       = models.CharField(max_length=50)
    gender     = models.CharField(max_length=10)
    birth_date = models.DateField()
    telnum     = models.CharField(max_length=11)
    zipcode    = models.CharField(max_length=5)

    base_addr  = models.CharField(max_length=255)
    dtl_addr   = models.CharField(max_length=255)