from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ApiToken(models.Model):
    access_token = models.TextField()
    referesh_token = models.TextField()
    token_type = models.CharField(max_length=100)
    expires_in = models.BigIntegerField()


class Investor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    investor_no = models.BigIntegerField()
    investor_id = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
